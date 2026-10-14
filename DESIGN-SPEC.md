# Averon Advocacia — especificação de identidade e site

## 1. Objetivo e escopo

Criar um site institucional de advocacia inspirado nas referências da pasta `ref`, preservando sua linguagem editorial, mas desenvolvendo composição, medidas, cores, marca e conteúdo próprios.

Nome criado para esta proposta: **Averon Advocacia**. Forma curta: **Averon**. O nome é uma proposta criativa; sua disponibilidade comercial e de domínio ainda não foi verificada.

Este documento especifica o design para implementação futura. O arquivo `PROMPTS-IMAGENS.md` contém a leitura dos elementos visuais, o prompt base e os prompts individuais. As dez imagens foram geradas com a ferramenta integrada `image_gen` e estão em `assets/images/`; os originais PNG foram preservados em `assets/images/originals/`. Dimensões e arquivos estão registrados em `assets/images/manifest.json`.

## 2. Referências identificadas

Os arquivos não possuem os nomes “branding” e “website-design”. O mapeamento foi feito pelo conteúdo visual:

| Papel | Arquivo | Dimensões |
| --- | --- | --- |
| Branding | `ref/607d90b8304da22841b7551261c0794e.jpg` | 735 × 488 px |
| Website-design | `ref/ad270c563e534a5ce62149b656d435c6.jpg` | 736 × 1104 px |

As cores e proporções abaixo são propostas de adaptação. A baixa resolução das referências não permite determinar fontes, códigos de cor ou medidas originais com precisão.

### Branding: leitura visual

- Grade de seis peças com bordô, bege dourado, creme e sombras escuras.
- Tipografia sem serifa com contraste entre linhas leves e palavras em negrito.
- Fotografia jurídica com iluminação dramática: profissional à mesa, martelo, balança e Justiça em biblioteca.
- Símbolos jurídicos tratados como objetos de destaque, com metal dourado e ambientes sóbrios.
- Filetes finos, molduras curvas, aspas e caixas de texto com cantos arredondados.
- Marca original pequena nos cantos; alguns elementos aparecem em árabe e inglês.

**Aplicação:** usar a atmosfera e a família cromática; substituir a marca original por Averon, usar português e criar um símbolo próprio. Não reproduzir os textos, inscrições, logotipo ou composição das peças.

### Website-design: leitura visual

- Página central sobre um cenário externo desfocado, provavelmente parte da apresentação do mockup.
- Cabeçalho discreto integrado ao hero.
- Hero claro, com gravura da Justiça à direita e nome do escritório em escala muito grande.
- Texto breve no canto inferior esquerdo e botão arredondado à direita.
- Seção de apresentação branca, espaçosa, organizada em três colunas.
- Seção de equipe azul, com retratos em preto e branco e título enorme na base.
- Faixa de retratos com quatro cartões completos e um quinto parcialmente visível.
- Um retrato desfocado com texto sobreposto, sugerindo um estado de interação.

**Aplicação:** manter a hierarquia editorial, o encontro entre imagem e título e o ritmo de espaços. Trocar o azul por bordô, alterar proporções, simplificar o título sobre a gravura e reorganizar a seção de equipe. Não incluir o cenário desfocado externo no site.

## 3. Direção de identidade

Personalidade: sóbria, clara, contemporânea e acolhedora. A aparência deve transmitir cuidado e precisão, sem excesso de símbolos jurídicos.

### Marca

- Assinatura principal: `AVERON`, com `ADVOCACIA` em linha secundária.
- Criar o lettering como texto ou vetor, preservando legibilidade em tamanhos pequenos.
- Símbolo proposto: um “A” geométrico aberto, com travessa fina, envolvido parcialmente por um arco. O arco pode sugerir equilíbrio sem desenhar uma balança literal.
- Não reutilizar o monograma, as inscrições ou a marca da referência.
- Versões: bordô sobre marfim; marfim sobre bordô; versão monocromática.
- Altura do conjunto no cabeçalho: aproximadamente 36 px no desktop e 30 px no mobile.
- Área de proteção mínima: metade da altura do símbolo. Largura mínima sugerida da assinatura completa: 120 px.

### Paleta proposta

| Token | Cor | Uso |
| --- | --- | --- |
| `--wine-900` | `#4A171E` | Footer, planos profundos e sombras gráficas |
| `--wine-700` | `#742B35` | Equipe, botões principais e assinatura |
| `--wine-500` | `#91434C` | Detalhes secundários e estados de interação |
| `--gold-500` | `#B69863` | Filetes, símbolos e pequenos acentos |
| `--sand-200` | `#E1CFAD` | Superfícies complementares |
| `--ivory-50` | `#F5F0E7` | Fundo principal e hero |
| `--paper-0` | `#FFFCF7` | Seção institucional e cartões claros |
| `--ink-900` | `#252321` | Texto sobre superfícies claras |
| `--stone-600` | `#66605A` | Texto secundário sobre superfícies claras |

Não usar dourado como cor de parágrafos pequenos sobre marfim. Usar texto marfim sobre bordô e tinta escura sobre fundos claros. Verificar contraste na implementação, incluindo estados de foco e hover; os tokens ainda não constituem uma auditoria de acessibilidade.

### Tipografia

- Títulos e palavra “Averon”: **Cormorant Garamond**, pesos 400/500; itálico apenas em palavras pontuais.
- Navegação, textos e botões: **Manrope**, pesos 400/500/600.
- Fallback de títulos: `Georgia, serif`; fallback de texto: `Arial, sans-serif`.
- Essas famílias são escolhas da proposta, não uma identificação das fontes nas imagens.
- Preferir fontes locais em WOFF2, com licença apropriada e `font-display: swap`.
- Título do hero: `clamp(76px, 12vw, 172px)`, entrelinha 0,88 e tracking de aproximadamente −0,045em.
- Títulos de seção: `clamp(42px, 5vw, 72px)`, entrelinha 1,02.
- Texto corrido: 16 px, entrelinha 1,65; introduções até 20 px.
- Navegação: 13–14 px; etiquetas: 11–12 px com espaçamento de 0,12em.

## 4. Grade e medidas

As medidas são parâmetros de implementação próprios, não cópias das medidas da referência.

| Parâmetro | Desktop ≥ 1200 px | Tablet 768–1199 px | Mobile < 768 px |
| --- | --- | --- | --- |
| Largura máxima do conteúdo | 1280 px | Fluida | Fluida |
| Margens laterais | 48 px | 32 px | 20 px |
| Colunas | 12 | 8 | 4 |
| Gutter | 24 px | 20 px | 16 px |
| Espaço vertical de seção | 104–120 px | 72–88 px | 56–64 px |
| Cabeçalho | 88 px | 80 px | 72 px |
| Hero, incluindo cabeçalho | Mínimo 740 px | Mínimo 660 px | Altura automática |

- Página ocupa a largura da janela; apenas o conteúdo interno recebe limite de largura.
- Escala de espaçamento: 4, 8, 12, 16, 24, 32, 48, 64, 88, 104 e 120 px.
- Botões com altura mínima de 48 px, padding horizontal de 24 px e raio de 999 px.
- Fotografias da equipe com raio de 0–4 px; evitar aparência de cartões de aplicativo.
- Filetes de 1 px, sem sombras pesadas em componentes.

## 5. Estrutura da página

### 5.1 Cabeçalho

Marca à esquerda, navegação à direita: `Escritório`, `Atuação`, `Equipe`, `Contato`. Links devem apontar para seções reais. Não inserir busca ou ícones de redes sem funcionalidade e destinos definidos.

No mobile, usar menu com botão identificado, estado expandido e operação por teclado. Logo e CTA devem permanecer legíveis.

### 5.2 Hero

Fundo marfim. Conteúdo em camadas, inspirado na gravura e na escala tipográfica da referência:

1. Etiqueta discreta: `AVERON ADVOCACIA`.
2. Palavra `Averon` em serifada monumental, ocupando aproximadamente 65% da largura útil.
3. Frase principal: `Clareza para decidir. Segurança para avançar.`
4. Texto de apoio: `Orientação jurídica com atenção ao contexto de cada decisão.`
5. CTA principal: `Conheça o escritório`, direcionado para a apresentação.
6. Gravura da Justiça à direita, em tinta bordô escura sobre transparência.

Desktop: arte com largura aproximada de 460–560 px, ancorada à direita e à base do hero. O título pode cruzar uma parte vazia da gravura, preservando leitura. Reservar uma zona segura para rosto, mão e balança.

Diferença deliberada: o título não atravessa o rosto da figura e o CTA fica junto ao texto, em vez de isolado sobre a imagem.

Mobile: texto primeiro, arte abaixo; título entre 76 e 104 px conforme espaço. Arte de aproximadamente 300–380 px de altura, com corte apenas na parte inferior da roupa. Sem sobreposição entre texto e rosto. Não forçar a altura de desktop.

### 5.3 Apresentação do escritório

Superfície clara, título `Uma atuação próxima. Uma visão estratégica.`

Desktop: três zonas, aproximadamente 30% / 25% / 45%: título, frase curta e parágrafo. Tablet: duas colunas. Mobile: uma coluna.

Texto proposto: `Cada questão jurídica envolve pessoas, prioridades e consequências. A Averon organiza informações e constrói caminhos com comunicação clara e atenção aos detalhes.`

Frase de apoio: `Escuta, análise e direção.`

Não inventar tempo de mercado, número de profissionais, prêmios, unidades ou resultados. Inserir dados reais apenas quando fornecidos.

### 5.4 Áreas de atuação — extensão proposta

Esta seção não aparece na captura. É uma extensão funcional para dar destino ao item “Atuação”.

Lista editorial com quatro posições de conteúdo, bordas finas e títulos de 24–28 px. Especialidades e descrições devem ser confirmadas pelo escritório; no protótipo usar `Área de atuação 01` a `04`, sem afirmar serviços ainda não definidos.

Sem fotos adicionais obrigatórias. Numeração e ícones devem ser texto ou SVG. Remover esta seção e o item de navegação caso o conteúdo não seja necessário.

### 5.5 Equipe

Fundo bordô `--wine-700`, texto marfim. Título `Pessoas por trás das decisões.` aparece **antes** dos retratos; a referência posiciona o grande título na base.

- Desktop: quatro retratos visíveis em uma grade, com navegação para o quinto quando houver carrossel. Como alternativa simples, grade com todos os integrantes e quebra de linha.
- Tablet: duas colunas. Mobile: uma coluna ou faixa horizontal com snap e controles acessíveis.
- Retratos verticais 4:5, preto e branco quente, enquadramento consistente.
- Nome abaixo da foto, serifada de aproximadamente 22 px; cargo em sans de 12–13 px.
- Protótipo: `Integrante 01` a `05`, com indicação `Perfil ilustrativo`.
- Não publicar pessoas geradas como integrantes reais. Na versão institucional, substituir por fotos, nomes e cargos autorizados.
- Interação: imagem pode receber leve redução de contraste, overlay bordô e link `Ver perfil`. Nada depende exclusivamente de hover.
- Desfoque é um efeito CSS opcional; não gerar um retrato já desfocado.
- Não adicionar link de perfil sem página ou painel com conteúdo real; no protótipo sem perfis, omitir o link.

### 5.6 Contato e rodapé — extensão proposta

Estas áreas não estão visíveis na referência. Acrescentar um fechamento simples para a navegação ter destino.

Contato sobre marfim: `Vamos conversar sobre o seu contexto.` Incluir canais reais quando fornecidos. Não inventar telefone, endereço, e-mail, inscrição profissional ou links de WhatsApp.

Rodapé em bordô profundo: marca, navegação curta e dados institucionais confirmados. Não acrescentar formulário sem definição de envio e tratamento dos dados.

## 6. Imagens e tratamento

### Obrigatórias para reproduzir a linguagem do site

| ID | Entrega proposta | Proporção | Tratamento |
| --- | --- | --- | --- |
| IMG-01 | `hero-justica.png` | 4:5 | Gravura original, fundo transparente |
| IMG-02 | `equipe-01.webp` | 4:5 | Retrato fictício para protótipo |
| IMG-03 | `equipe-02.webp` | 4:5 | Retrato fictício para protótipo |
| IMG-04 | `equipe-03.webp` | 4:5 | Retrato fictício para protótipo |
| IMG-05 | `equipe-04.webp` | 4:5 | Retrato fictício para protótipo |
| IMG-06 | `equipe-05.webp` | 4:5 | Retrato fictício para protótipo |

O quinto cartão da referência é parcial. Seu retrato será uma interpretação nova; não é possível inferir a aparência completa. O terceiro está desfocado, então o prompt também propõe uma pessoa original.

### Complementares para a identidade

| ID | Entrega proposta | Proporção | Uso |
| --- | --- | --- | --- |
| IMG-07 | `branding-mesa-juridica.webp` | 4:3 | Comunicação institucional |
| IMG-08 | `branding-martelo.webp` | 1:1 | Peça de marca ou apoio |
| IMG-09 | `branding-balanca.webp` | 1:1 | Peça de marca ou apoio |
| IMG-10 | `branding-justica-biblioteca.webp` | 4:5 | Comunicação ou apresentação |

Essas quatro imagens reinterpretam os assuntos fotográficos do branding. Não são necessárias no layout principal e não devem competir com a gravura do hero.

Logotipo, títulos, botões, aspas, molduras e blocos coloridos devem ser construídos em texto, CSS ou SVG. Não solicitar sua renderização dentro das fotografias.

## 7. Interação, acessibilidade e entrega técnica

- Header acompanha o fluxo; se for fixo, ajustar âncoras para que títulos não fiquem ocultos.
- Transições discretas de 160–240 ms. Respeitar `prefers-reduced-motion`.
- Foco de teclado visível e áreas de toque de pelo menos 44 × 44 px.
- Um único H1; demais títulos seguem hierarquia sem escolher nível apenas pelo tamanho.
- Se a gravura for puramente decorativa, usar `alt=""`; retratos reais recebem descrição adequada.
- Contraste mínimo de 4,5:1 para texto normal e 3:1 para texto grande; verificar os componentes finais.
- Não depender do texto embutido em imagem para apresentar conteúdo do site.
- Gravura em PNG/WebP com alpha; fotografias em WebP/AVIF após exportação e revisão.
- Reservar dimensões de imagens para evitar saltos de layout; carregar o hero com prioridade e retratos abaixo da dobra com lazy loading.
- Usar `object-fit: cover` nos retratos, com posição ajustada por imagem para preservar os rostos.

## 8. Critérios de revisão

1. Identidade Averon presente em todos os locais de marca; nenhuma inscrição da referência original.
2. Paleta bordô, dourado e marfim; azul da referência do site substituído.
3. Hero mantém gravura e tipografia grande, com composição própria e leitura preservada.
4. Seções claras e bordô alternadas, com espaçamento generoso.
5. Retratos com proporção e tratamento consistentes; perfis fictícios sinalizados no protótipo.
6. Em 360, 768 e 1440 px, não há rolagem horizontal acidental, sobreposição ilegível ou cortes de rosto.
7. Navegação e CTA têm destinos reais; dados não fornecidos permanecem como conteúdo pendente.
8. Não há promessas de resultados, números inventados ou fotos geradas apresentadas como pessoas reais.
9. Imagens e layout dialogam com as referências sem reproduzir sua marca e composição integral.

## 9. Prompt base para implementar o site

Copiar este texto para o agente que realizará a implementação, junto com este documento, as referências e as imagens aprovadas:

```text
Implemente um site institucional responsivo para Averon Advocacia conforme DESIGN-SPEC.md. Use ref/607d90b8304da22841b7551261c0794e.jpg como referência de atmosfera e identidade, e ref/ad270c563e534a5ce62149b656d435c6.jpg como referência de hierarquia editorial e estrutura de página. Crie uma interpretação própria, sem duplicar marca, textos, composição ou proporções exatas.

Use bordô #742B35, bordô profundo #4A171E, dourado fosco #B69863, marfim #F5F0E7 e tinta #252321. Títulos em Cormorant Garamond e texto em Manrope, com fallbacks. A marca deve ser AVERON / ADVOCACIA em texto ou vetor, acompanhada por um monograma A original.

Monte cabeçalho, hero com gravura da Justiça e título Averon em grande escala, apresentação espaçosa, áreas de atuação com conteúdo pendente, equipe em fundo bordô, contato e rodapé. Use o texto e as medidas da especificação. As seções de atuação, contato e rodapé são extensões propostas, ausentes da captura original.

Use hero-justica.png e os cinco retratos aprovados conforme o manifesto de imagens. Os retratos gerados são fictícios e devem ser sinalizados como Perfil ilustrativo no protótipo. Não invente informações profissionais ou contatos. Não coloque texto dentro das fotos. Construa efeitos de hover, linhas, molduras e fundos em CSS/SVG.

Garanta hierarquia semântica, operação por teclado, foco visível, contraste verificado, redução de movimento e funcionamento em 360, 768 e 1440 px. Não publique nem trate a proposta como site institucional final antes de substituir conteúdo pendente e confirmar os dados do escritório.
```
