"""Export generated PNG sources to the project's image manifest (GIMP Python)."""
import ctypes
import json
import shutil
from pathlib import Path

import gi

gi.require_version("GdkPixbuf", "2.0")
from gi.repository import GdkPixbuf

root = Path(__file__).resolve().parents[1]
folder = root / "assets" / "images"
manifest = json.loads((folder / "generation-sources.json").read_text(encoding="utf-8"))
originals = folder / "originals"
originals.mkdir(exist_ok=True)
webp = ctypes.CDLL("libwebp-7.dll")
for name in ("WebPEncodeRGB", "WebPEncodeRGBA"):
    fn = getattr(webp, name)
    fn.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int,
                   ctypes.c_float, ctypes.POINTER(ctypes.c_void_p)]
    fn.restype = ctypes.c_size_t
webp.WebPFree.argtypes = [ctypes.c_void_p]
webp.WebPGetInfo.argtypes = [ctypes.c_void_p, ctypes.c_size_t,
                           ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int)]
webp.WebPGetInfo.restype = ctypes.c_int

for asset in manifest["assets"]:
    source = Path(asset["source"])
    original = originals / (asset["name"] + ".png")
    target = folder / asset["file"]
    if original.exists() or target.exists():
        raise FileExistsError(f"Refusing to overwrite: {target}")
    shutil.copy2(source, original)
    pixbuf = GdkPixbuf.Pixbuf.new_from_file(str(original))
    width, height = pixbuf.get_width(), pixbuf.get_height()
    pixels = pixbuf.get_pixels()
    if target.suffix == ".png":
        assert pixbuf.get_has_alpha(), "Hero must have alpha"
        assert min(pixels[3::4]) == 0, "Hero must contain transparent pixels"
        shutil.copy2(original, target)
    else:
        buffer = ctypes.create_string_buffer(pixels)
        output = ctypes.c_void_p()
        fn = webp.WebPEncodeRGBA if pixbuf.get_has_alpha() else webp.WebPEncodeRGB
        count = fn(buffer, width, height, pixbuf.get_rowstride(), 90.0,
                   ctypes.byref(output))
        if not count:
            raise RuntimeError(f"WebP export failed: {target}")
        try:
            encoded = ctypes.string_at(output, count)
        finally:
            webp.WebPFree(output)
        check_width, check_height = ctypes.c_int(), ctypes.c_int()
        assert webp.WebPGetInfo(encoded, len(encoded), ctypes.byref(check_width),
                               ctypes.byref(check_height))
        assert (check_width.value, check_height.value) == (width, height)
        target.write_bytes(encoded)
    asset.update(width=width, height=height, bytes=target.stat().st_size,
                 original=f"originals/{original.name}",
                 transparent=pixbuf.get_has_alpha() if target.suffix == ".png" else False)
    print(f"{target.name}: {width}x{height}, {target.stat().st_size:,} bytes")

manifest["export"] = "Original size; PNG alpha preserved; photographic WebP quality 90"
(folder / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2),
                                     encoding="utf-8")
