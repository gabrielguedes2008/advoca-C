# Averon Advocacia — leitura visual e prompts de imagens

## 1. Como usar no GPT

Este arquivo contém **um prompt base e dez prompts individuais**: uma gravura, cinco retratos e quatro fotografias complementares. As seis primeiras imagens atendem ao layout; as quatro últimas ampliam a identidade visual.

Para cada geração, enviar **PROMPT BASE + PROMPT INDIVIDUAL** na mesma mensagem. Os nomes de arquivo são destinos de exportação, não texto para aparecer nas imagens. Solicitar a proporção indicada; se a ferramenta não aceitar a resolução sugerida, usar a maior dimensão disponível na mesma proporção e exportar depois.

Anexos opcionais: a imagem de branding ajuda a comunicar a atmosfera. Para a gravura e os retratos, a captura do site ajuda a comunicar o tipo de imagem. Pedir uma composição original, sem copiar rostos, marca ou inscrições. Após aprovar o primeiro retrato, anexá-lo aos próximos como referência de iluminação e enquadramento, mantendo identidades diferentes.

A geração em lote pode variar em estilo. Cada imagem recebeu uma chamada individual à ferramenta integrada `image_gen`, usando exatamente o prompt base e o respectivo prompt individual deste documento. As dez imagens estão salvas em `assets/images/`, com originais PNG em `assets/images/originals/` e registro em `assets/images/manifest.json`.

## 2. Leitura de todas as imagens e elementos das referências

### Referência de site

Arquivo: `ref/ad270c563e534a5ce62149b656d435c6.jpg`.

| Elemento observado | Leitura | Decisão para Averon |
| --- | --- | --- |
| Gravura principal | Figura feminina clássica da Justiça, mão elevada segurando balança, drapeado e traços de gravura; ocupa a metade direita | IMG-01: nova gravura em bordô, isolada e transparente |
| Retrato 1 | Pessoa com cabelo escuro, óculos e blazer, em preto e branco | IMG-02: personagem fictícia distinta, com linguagem equivalente |
| Retrato 2 | Pessoa com cabelo curto e barba, terno e braços cruzados | IMG-03: personagem fictício distinto, pose própria |
| Retrato 3 | Pessoa com cabelo longo, imagem desfocada e texto sobreposto | IMG-04: retrato nítido original; desfoque e texto feitos no site |
| Retrato 4 | Pessoa com cabelo longo, blazer escuro, blusa clara e braços cruzados | IMG-05: personagem fictícia distinta, pose adaptada |
| Retrato 5 | Parte de um retrato aparece cortada na borda direita | IMG-06: interpretação nova, pois a figura inteira não é visível |
| Cenário externo | Ambiente desfocado atrás do retângulo da página | Não gerar: parece ser cenário do mockup, sem função no site |
| Fundos, botão e textos | Superfícies claras, faixa azul, tipografia e navegação | Construir em CSS/HTML, com a paleta Averon |

Não é possível identificar as pessoas, os arquivos originais nem a aparência do retrato desfocado com precisão. Os prompts não tentam reproduzir essas identidades.

### Referência de branding

Arquivo: `ref/607d90b8304da22841b7551261c0794e.jpg`.

| Peça da grade | Leitura | Decisão para Averon |
| --- | --- | --- |
| Superior esquerda | Profissional de terno à mesa, mãos unidas, documentos e objetos jurídicos, luz dramática | IMG-07: fotografia editorial nova |
| Superior central | Placa bordô em fundo bege, moldura, aspas e texto de marca | Não gerar como fotografia; recriar placa, moldura e texto em vetor/CSS |
| Superior direita | Martelo jurídico escuro com metal dourado sobre pedestal, fundo vermelho | IMG-08: natureza-morta original |
| Inferior esquerda | Balão/caixa bordô com aspas, frase clara e filetes curvos sobre bege | Não gerar como fotografia; composição gráfica em vetor/CSS |
| Inferior central | Balança dourada contra fundo bordô, com uma parte da estrutura cortada | IMG-09: balança com composição própria |
| Inferior direita | Estátua da Justiça em biblioteca, iluminação quente e filtro vermelho | IMG-10: fotografia original de escultura em ambiente jurídico |

As peças gráficas de texto não exigem arquivos gerados. Para materiais futuros, usar a marca Averon e frases reais em português sobre os fundos da identidade. Não reproduzir o inglês, o árabe ou o nome da referência.

## 3. Prompt base de direção visual

Copiar integralmente e acrescentar um dos prompts da próxima seção:

```text
Crie uma imagem original para a identidade de Averon Advocacia, um escritório jurídico com estética editorial sóbria e contemporânea. A direção visual combina bordô profundo, dourado fosco, marfim e tons neutros quentes. Referências cromáticas: #4A171E, #742B35, #B69863, #E1CFAD, #F5F0E7 e #252321. Use esses valores como orientação de cor; não como texto na imagem.

Priorize composição limpa, materiais verossímeis, detalhes refinados e contraste controlado. Evite saturação excessiva, brilho plástico, aparência de publicidade genérica e filtros pesados. A imagem deve funcionar em um site com títulos serifados grandes e bastante espaço em branco.

Quando o pedido for fotografia, produza fotografia editorial realista com luz suave e textura natural. Quando for gravura, use traço de gravura original com hachuras, sem estética fotográfica. Quando for retrato, mantenha preto e branco de temperatura ligeiramente quente, sem aplicar bordô à pele. O prompt individual determina o fundo, a proporção e o enquadramento; nos retratos, o fundo neutro prevalece sobre a paleta geral.

Não inclua palavras, letras, marca, logotipo, assinatura, números, molduras gráficas nem marca-d'água. Não copie a composição exata das referências. Gere somente a imagem individual solicitada, sem colagem ou mockup de página. Personagens humanos devem ser fictícios e diferentes das pessoas visíveis nas referências. Preserve anatomia, mãos, olhos e objetos com estrutura coerente.
```

## 4. Prompts individuais — imagens do site

### IMG-01 — gravura da Justiça

- Arquivo: `hero-justica.png`.
- Proporção: 4:5; resolução sugerida: 1600 × 2000 px.
- Fundo: transparente real, com canal alpha; não simular transparência com quadriculado.
- Uso: lado direito do hero sobre marfim.

```text
Gere uma ilustração original da Justiça em linguagem de gravura calcográfica clássica. Figura feminina adulta, expressão serena, rosto descoberto, cabelo preso com ondas discretas e túnica drapeada. Mostre da cabeça até abaixo da cintura, com tecido suficiente na base para permitir corte no layout. Um braço elevado sustenta uma pequena balança de dois pratos com correntes fisicamente coerentes; o outro segura uma espada parcialmente visível apontada para baixo, sem gesto agressivo.

Composição vertical 4:5. A figura ocupa aproximadamente 80% da altura e fica deslocada para a direita. Reserve alguma área livre à esquerda; mantenha cabeça, mão elevada e balança inteiras, com pelo menos 6% de margem superior. Crie uma pose e desenho diferentes da gravura de referência.

Use linhas finas, hachuras e variação de densidade para volume, com tinta bordô muito escura próxima de #4A171E. Sem grandes massas de preto, sem preenchimento branco opaco no entorno, sem brilho metálico fotográfico. Contorno limpo, detalhes legíveis em tamanho de site e sem halo claro nas bordas.

Isole a figura em fundo verdadeiramente transparente. Não inclua cenário, pedestal, texto, moldura ou textura de papel no fundo. O estilo deve parecer uma gravura histórica reinterpretada, sem envelhecimento artificial excessivo.
```

### IMG-02 — equipe, perfil ilustrativo 01

- Arquivo final: `equipe-01.webp`.
- Proporção: 4:5; resolução sugerida: 1200 × 1500 px.
- Uso: primeiro cartão; pessoa fictícia.

```text
Crie um retrato editorial fotográfico de uma profissional jurídica fictícia com aproximadamente 40 anos, cabelo escuro na altura dos ombros e óculos de armação fina. Identidade facial original, sem reproduzir a pessoa da referência. Blazer de alfaiataria escuro, blusa clara sem estampas, expressão tranquila e pequeno sorriso natural.

Enquadramento vertical 4:5, da cabeça até o início dos quadris. Corpo levemente em três quartos, rosto voltado para a câmera, braços relaxados; mantenha mãos fora do enquadramento. Fundo uniforme cinza-claro quente, sem objetos. Luz ampla e suave vindo da esquerda da câmera, sombras discretas, sem recorte luminoso artificial.

Fotografia em preto e branco com temperatura ligeiramente quente, textura de pele natural e tecido visível. Lente com aparência de retrato de 85 mm, sem distorção facial. Cabeça centralizada horizontalmente, olhos aproximadamente a 28% da altura a partir do topo e espaço de 8% acima do cabelo. Pessoa ocupa aproximadamente 75% da largura. Imagem totalmente nítida, sem texto e sem marca.
```

### IMG-03 — equipe, perfil ilustrativo 02

- Arquivo final: `equipe-02.webp`.
- Proporção: 4:5; resolução sugerida: 1200 × 1500 px.
- Uso: segundo cartão; pessoa fictícia.

```text
Crie um retrato editorial fotográfico de um profissional jurídico fictício com aproximadamente 38 anos, cabelo curto e barba curta bem cuidada. Identidade facial original. Terno grafite, camisa clara e gravata discreta. Expressão confiante e acolhedora, sem pose autoritária. Corpo levemente em três quartos, ombros relaxados e braços cruzados de forma natural, mãos e dedos anatomicamente corretos.

Enquadramento vertical 4:5, da cabeça até o início dos quadris. Fundo uniforme cinza-claro quente, sem escritório ou objetos. Luz ampla e suave vindo da esquerda da câmera, com sombras discretas. Preto e branco de temperatura ligeiramente quente, textura real de pele e tecido, sem retoque plástico.

Mantenha a mesma escala e iluminação dos demais retratos: cabeça centralizada, olhos aproximadamente a 28% da altura a partir do topo, margem de 8% acima do cabelo, pessoa ocupando aproximadamente 75% da largura. Aparência de lente de retrato de 85 mm, sem distorção. Sem texto, logotipo ou marca-d'água.
```

### IMG-04 — equipe, perfil ilustrativo 03

- Arquivo final: `equipe-03.webp`.
- Proporção: 4:5; resolução sugerida: 1200 × 1500 px.
- Uso: terceiro cartão; a versão desfocada será feita em CSS.

```text
Crie um retrato editorial fotográfico inteiramente nítido de uma profissional jurídica fictícia com aproximadamente 34 anos, cabelo castanho ondulado de comprimento médio, blazer escuro e blusa de gola simples. Crie uma identidade facial própria; o retrato desfocado da referência serve apenas para entender o formato do cartão, não para reconstruir uma pessoa.

Enquadramento vertical 4:5, da cabeça até o início dos quadris. Postura frontal, leve sorriso, ombros relaxados, mãos fora do enquadramento. Fundo uniforme cinza-claro quente. Luz ampla e suave da esquerda da câmera. Preto e branco com leve temperatura quente, pele natural e contraste médio.

Alinhe o rosto aos demais retratos: olhos aproximadamente a 28% da altura a partir do topo, 8% de margem acima do cabelo, pessoa ocupando aproximadamente 75% da largura. Aparência de lente de retrato de 85 mm. Não aplique desfoque, sobreposição de cor, texto ou efeitos de interação. Sem marca ou acessórios chamativos.
```

### IMG-05 — equipe, perfil ilustrativo 04

- Arquivo final: `equipe-04.webp`.
- Proporção: 4:5; resolução sugerida: 1200 × 1500 px.
- Uso: quarto cartão; pessoa fictícia.

```text
Crie um retrato editorial fotográfico de uma profissional jurídica fictícia com aproximadamente 42 anos, cabelo longo liso preso parcialmente atrás de uma orelha, blazer escuro e camisa clara com gola aberta discreta. Identidade facial original, diferente das referências e dos outros retratos. Expressão atenta e sorriso suave. Corpo ligeiramente em três quartos, braços cruzados de maneira relaxada, com mãos naturais e dedos corretos.

Enquadramento vertical 4:5, da cabeça até o início dos quadris. Fundo uniforme cinza-claro quente, luz ampla e suave da esquerda da câmera, preto e branco de temperatura ligeiramente quente. Preserve textura da pele, pequenas linhas de expressão e detalhes do tecido.

Cabeça centralizada, olhos aproximadamente a 28% da altura a partir do topo, espaço de 8% acima do cabelo e pessoa ocupando aproximadamente 75% da largura. Aparência de lente de retrato de 85 mm. Imagem nítida, sem filtros pesados, texto, marca ou elementos do escritório ao fundo.
```

### IMG-06 — equipe, perfil ilustrativo 05

- Arquivo final: `equipe-05.webp`.
- Proporção: 4:5; resolução sugerida: 1200 × 1500 px.
- Uso: quinto cartão; interpretação do cartão parcial.

```text
Crie um retrato editorial fotográfico de um profissional jurídico fictício com aproximadamente 50 anos, cabelo curto com fios grisalhos, rosto sem barba, blazer escuro e camisa clara sem gravata. Crie uma pessoa totalmente original: a referência mostra apenas uma parte do quinto cartão e não deve definir sua identidade. Expressão serena, postura frontal e ombros relaxados. Mãos fora do enquadramento.

Enquadramento vertical 4:5, da cabeça até o início dos quadris, sem cortar a pessoa lateralmente na imagem original. Fundo uniforme cinza-claro quente, luz ampla e suave vindo da esquerda da câmera. Fotografia em preto e branco de temperatura ligeiramente quente, pele natural, sem suavização excessiva.

Mantenha consistência com os demais retratos: olhos aproximadamente a 28% da altura a partir do topo, margem de 8% acima do cabelo e pessoa ocupando aproximadamente 75% da largura. Aparência de lente de retrato de 85 mm. Sem texto, logotipo ou marca-d'água. Qualquer corte lateral será feito pelo layout, não na geração.
```

## 5. Prompts individuais — imagens complementares do branding

Estas imagens são opcionais no site. Podem apoiar peças de comunicação com texto aplicado posteriormente. Não gerar as seis peças da referência como uma colagem.

### IMG-07 — mesa jurídica

- Arquivo final: `branding-mesa-juridica.webp`.
- Proporção: 4:3; resolução sugerida: 1600 × 1200 px.

```text
Crie uma fotografia editorial original de uma pessoa profissional jurídica fictícia sentada atrás de uma mesa de madeira escura. Enquadramento do peito até a mesa, sem mostrar o rosto. Terno grafite, camisa clara e gravata bordô discreta. Mãos repousam naturalmente uma sobre a outra, com anatomia correta, em uma pose diferente das mãos entrelaçadas da referência.

Sobre a mesa, uma pasta de documentos sem texto legível, uma caneta e uma pequena balança de latão fosco em segundo plano. Ambiente sóbrio, luz quente lateral, sombras profundas com detalhes preservados e toque bordô muito sutil. Madeira e metal realistas, sem brilho plástico.

Formato horizontal 4:3. Posicione pessoa e objetos prioritariamente na metade direita e inferior; deixe o terço superior esquerdo escuro e visualmente tranquilo para aplicar uma chamada depois. Não inclua palavras, logotipos, inscrições jurídicas, carimbos nem telas. Não transforme a cena em uma cópia da composição original.
```

### IMG-08 — martelo jurídico

- Arquivo final: `branding-martelo.webp`.
- Proporção: 1:1; resolução sugerida: 1600 × 1600 px.

```text
Crie uma natureza-morta fotográfica editorial de um martelo jurídico de madeira escura com uma faixa estreita de latão escovado, apoiado diagonalmente ao lado de um bloco de madeira baixo e circular. O objeto é simbólico para comunicação visual, sem representar um procedimento jurídico específico.

Fundo de estúdio bordô profundo próximo de #742B35, superfície em bordô mais escuro e luz quente suave vinda de cima à esquerda. Madeira com veios naturais, metal dourado fosco, sombra de contato realista e composição sóbria. Martelo e bloco devem estar completamente visíveis, com proporções coerentes.

Formato quadrado 1:1. Concentre os objetos na metade inferior direita, deixando espaço limpo na parte superior esquerda para texto posterior. Use enquadramento e posição diferentes da referência. Sem texto, logotipo, marca-d'água, reflexos espelhados excessivos ou objetos adicionais.
```

### IMG-09 — balança

- Arquivo final: `branding-balanca.webp`.
- Proporção: 1:1; resolução sugerida: 1600 × 1600 px.

```text
Crie uma fotografia editorial de uma balança jurídica de latão fosco com dois pratos, estrutura simples e elegante. Mostre a haste central, a travessa, os dois conjuntos de correntes e os dois pratos com construção fisicamente coerente. Os pratos ficam aproximadamente equilibrados, sem correntes duplicadas ou partes suspensas sem apoio.

Fundo de estúdio bordô profundo próximo de #742B35, com gradiente muito discreto. Luz suave lateral valoriza o metal dourado envelhecido sem aparência enferrujada. Contraste moderado, sombra suave e detalhes refinados.

Composição quadrada 1:1, objeto deslocado para a direita, inteiramente visível e ocupando aproximadamente 65% da altura. Reserve o terço esquerdo mais livre para aplicação posterior de texto. Não copie o corte da balança da referência. Sem texto, marca, símbolos gravados ou moldura.
```

### IMG-10 — Justiça em biblioteca

- Arquivo final: `branding-justica-biblioteca.webp`.
- Proporção: 4:5; resolução sugerida: 1600 × 2000 px.

```text
Crie uma fotografia editorial original de uma escultura clássica da Justiça em bronze escuro com nuances douradas, em uma biblioteca de arquitetura sóbria. Figura com venda delicada, túnica drapeada e balança visível; espada apontada para baixo pode aparecer parcialmente. Não reproduza uma escultura identificável ou a composição exata da referência.

Enquadramento vertical 4:5, da cabeça até a cintura ou pedestal superior. Posicione a escultura no lado direito, com rosto e mão completos. Ao fundo, estantes de madeira escura e livros sem títulos legíveis, desfocados moderadamente. Luz quente lateral, reflexos controlados no bronze e presença sutil de bordô nas sombras.

Reserve o quadrante superior esquerdo com menor complexidade visual para texto posterior. A imagem deve parecer fotografia de uma escultura real, sem pele humana, sem aparência de render plástico e sem filtro vermelho intenso. Correntes e pratos da balança devem ter estrutura consistente. Sem palavras, marcas, molduras ou marca-d'água.
```

## 6. Revisão e correções no GPT

Verificar cada resultado na resolução de exportação e também em tamanho pequeno, próximo ao uso no site:

- Gravura: rosto e mão inteiros; balança coerente; fundo realmente transparente; bordas sem halo.
- Retratos: pessoas distintas, mesma escala, fundo e direção de luz; anatomia correta; nitidez e textura natural.
- Objetos: correntes, pratos, cabo e base com geometria plausível; metal sem brilho plástico.
- Composição: espaço para texto nos lugares solicitados; ausência de letras e marcas acidentais.
- Paleta: bordô e dourado contidos nas cenas de marca; retratos continuam neutros.

Prompt de correção reutilizável, substituindo os campos entre colchetes:

```text
Edite a imagem anexada preservando identidade do personagem ou objeto, estilo, enquadramento e proporção. Corrija somente [PROBLEMA CONCRETO]. Mantenha [CARACTERÍSTICAS APROVADAS]. Não adicione texto, logotipo, objetos ou filtros. Preserve o fundo transparente quando ele existir. Entregue a mesma imagem com a correção, sem montar uma nova peça ou colagem.
```

Exemplo para consistência dos retratos:

```text
Use o retrato aprovado anexado apenas como referência de luz, fundo e escala. Ajuste este outro retrato para fundo cinza-claro quente, luz suave da esquerda e olhos na mesma altura relativa. Preserve a identidade própria desta pessoa, sua roupa e sua expressão. Não copie o rosto da referência. Mantenha proporção 4:5, nitidez e textura natural, sem texto.
```

## 7. Manifesto final de arquivos

Os dez arquivos abaixo foram gerados e exportados em `assets/images/`. A gravura mantém transparência real, verificada pelo canal alpha; as nove fotografias foram exportadas em WebP com qualidade 90, preservando suas dimensões originais.

Dimensões efetivamente entregues: gravura, retratos e biblioteca em 1122 × 1402 px (aproximadamente 4:5); mesa em 1448 × 1086 px (4:3); martelo e balança em 1254 × 1254 px. As dimensões sugeridas nos prompts são alvos de geração, e não as resoluções finais produzidas pela ferramenta. Nenhuma imagem foi ampliada artificialmente.

```text
assets/images/hero-justica.png
assets/images/equipe-01.webp
assets/images/equipe-02.webp
assets/images/equipe-03.webp
assets/images/equipe-04.webp
assets/images/equipe-05.webp
assets/images/branding-mesa-juridica.webp
assets/images/branding-martelo.webp
assets/images/branding-balanca.webp
assets/images/branding-justica-biblioteca.webp
```

Guardar também os originais gerados antes de converter para WebP. Conversão, compressão e redimensionamento são etapas de exportação, não texto que deve aparecer na imagem. Revisar novamente rostos e linhas finas depois da compressão.
