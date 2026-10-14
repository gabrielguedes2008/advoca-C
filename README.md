# Averon Advocacia

Site institucional estático, baseado em [DESIGN-SPEC.md](DESIGN-SPEC.md) e nas imagens geradas para esta proposta.

Site publicado com acesso privado: https://averon-advocacia.blushgoat32.chatgpt.site

## Executar localmente

Com Node.js instalado, na raiz deste projeto:

```sh
node site/server.mjs
```

Abra `http://127.0.0.1:4173`. Não há dependências npm ou etapa de compilação. Alternativamente, execute `npm run dev` dentro de `site/`.

## Estrutura

- `site/dist/`: arquivos estáticos prontos para hospedagem.
- `site/dist/index.html`: conteúdo da página.
- `site/dist/styles.css`: identidade visual e responsividade.
- `site/dist/app.js`: menu mobile, navegação e carrossel acessível.
- `site/dist/assets/`: imagens, fontes locais e favicon.
- `assets/images/`: imagens geradas e originais preservados.

Validação: `npm run check` dentro de `site/`.

No PowerShell com execução de scripts restrita, use `npm.cmd run check`. As verificações de caminhos de imagens/fontes, âncoras, sintaxe JavaScript e contrastes principais passaram; a resposta HTTP local foi 200. A revisão visual e os testes de interação em navegador não foram realizados porque nenhum navegador conectado estava disponível nesta sessão.

Para a publicação no Windows, o empacotador oficial do Sites precisou de Git Bash no PATH, `TAR_OPTIONS=--force-local` e Git com backend TLS OpenSSL. O empacotamento fora do sandbox também usou `safe.directory` limitado ao checkout `site/`, somente no ambiente do processo. Nenhuma configuração global do Git foi alterada.

A proposta usa retratos fictícios, identificados como ilustrativos. Especialidades e canais de contato aguardam informações reais. Nenhum formulário ou canal de atendimento simulado foi incluído.
