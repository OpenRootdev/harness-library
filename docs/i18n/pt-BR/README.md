<p align="center"><img src="../../../site/assets/mark.svg" width="70" alt="Harness Library"></p>
<h1 align="center">Harness Library</h1>
<p align="center"><a href="../../../README.md">English</a> · <a href="../es/README.md">Español</a> · <a href="../zh-CN/README.md">简体中文</a> · <a href="../fr/README.md">Français</a> · <a href="../ja/README.md">日本語</a> · <a href="../de/README.md">Deutsch</a> · <a href="README.md">Português (Brasil)</a></p>
<p align="center">Descubra, instale e compartilhe harnesses reutilizáveis para agentes.</p>
<p align="center"><a href="https://openrootdev.github.io/harness-library/">Explorar a biblioteca</a> · <a href="https://github.com/OpenRootdev/harness-library/issues/new?template=submit-harness.yml">Enviar um harness</a> · <a href="CONTRIBUTING.md">Guia de envio</a></p>

Um diretório aberto de instruções, habilidades, ferramentas e fluxos de trabalho que ajudam um agente a executar bem uma tarefa específica. Um harness pode consistir em poucos arquivos ou em uma configuração de ferramentas mais ampla. Cada entrada explica como instalá-lo, o que configurar manualmente e qual parte do repositório de origem é necessária.

As primeiras entradas são [Smooth Motion Graphics](https://github.com/Ker102/smooth-motion-graphics) e [ViperMesh for Blender](https://github.com/OpenRootdev/vipermesh-blender). O repositório e os lançamentos existentes do ViperMesh são listados sem alterações. Harneloop é opcional; harnesses criados com ele podem exibir essa atribuição após a revisão.

## Veja um harness em ação

O vídeo explicativo do Harneloop mostra o estilo de animação por trás do [harness Smooth Motion Graphics](https://openrootdev.github.io/harness-library/harnesses/smooth-motion-graphics/) da biblioteca: cenas legíveis, conexões curvas e transições suaves. Ele também explica como o Harneloop constrói e melhora unidades de harness.

<p align="center"><a href="https://harneloop.kaelux.dev/media/harneloop-how-it-works.mp4"><img src="https://harneloop.kaelux.dev/media/harneloop-video-poster.png" alt="Assista à demonstração silenciosa de motion graphics do Harneloop" width="860"></a></p>
<p align="center"><a href="https://harneloop.kaelux.dev/media/harneloop-how-it-works.mp4">Assista ao vídeo completo · 3:40 · Sem som, com explicações na tela</a></p>

O vídeo é hospedado separadamente. Acesse o pacote de instalação do próprio harness e seu renderizador de exemplo pela entrada correspondente.

## Envie um harness

**Novos envios são bem-vindos.** Procuramos harnesses úteis para programação, pesquisa, dados, trabalho criativo, Blender e operações. Algumas habilidades podem ser suficientes; não é necessário usar Harneloop.

1. [Abra o formulário curto de envio no GitHub](https://github.com/OpenRootdev/harness-library/issues/new?template=submit-harness.yml) e informe seu repositório e a tarefa que ele ajuda um agente a realizar.
2. Inclua passos claros de instalação, categoria, licença, escopo de versão/distribuição e qualquer configuração manual. Contagens de componentes e evidências de testes são opcionais.
3. Um mantenedor revisa a configuração, pede esclarecimentos na sua issue se necessário e publica as entradas aprovadas.

**Não é necessário fazer fork, abrir pull request ou ter uma conta do Harness Library.** O formulário exige uma conta do GitHub. Você também pode enviar uma PR adicionando um arquivo JSON a `data/listings/`. Veja o [guia público de envio](https://openrootdev.github.io/harness-library/submit/), [CONTRIBUTING.md](CONTRIBUTING.md) e [o modelo](../../../docs/listing.example.json).

Um repositório com conteúdo misto deve fornecer um pacote específico ou uma branch dedicada ao harness. Quem envia não define rótulos de verificação ou promoção. Os mantenedores revisam configuração, escopo e eventuais evidências antes de publicar a entrada. “Artifacts checked” significa que os artefatos documentados foram inspecionados; não implica que todos os modelos, plataformas ou casos de uso funcionem.

## Programa gratuito de badges

Adicione o badge exato “Listed in Harness Library” e o link de retorno à entrada nas primeiras 30 linhas do README de origem. Após a verificação, sua entrada recebe **um único destaque comunitário de 14 dias**, claramente identificado no diretório. O destaque afeta a ordenação, não o status da revisão. É gratuito, opcional e expira automaticamente. Remover e adicionar novamente o badge não reinicia o período. [Política e verificação](docs/badge-program.md).

## Desenvolvimento

Não são necessárias dependências de frontend nem um serviço de backend. Python 3.11+ executa o validador e o gerador; a interface usa HTML, CSS e JavaScript simples.

```sh
python scripts/catalog.py validate
python -m unittest discover -s tests -v
python scripts/catalog.py build
python -c "import shutil; shutil.copytree('dist', '.preview/harness-library', dirs_exist_ok=True)"
python -m http.server 4201 --directory .preview
```

Abra `http://localhost:4201/harness-library/`. A cópia de prévia serve corretamente o caminho base de produção; atualize-a após uma nova geração. Os caminhos de recursos e navegação correspondem intencionalmente à URL do projeto no GitHub Pages.

`site/layout.html`, `site/style.css` e `scripts/publishing.py` geram páginas HTML completas para o diretório, cada harness, o guia de envio e a página sobre o projeto. JavaScript adiciona progressivamente busca, filtros e cópia; o conteúdo de instalação e a navegação continuam utilizáveis sem ele. As gerações também publicam um sitemap, espelhos Markdown das páginas, `llms.txt` e o catálogo JSON revisado. Veja [Descoberta e indexação](docs/discovery.md) para a configuração do proprietário e os detalhes de rastreamento.

`python scripts/catalog.py refresh` verifica os badges de quem optou por participar lendo o conteúdo público dos READMEs no GitHub. Ele nunca executa código enviado. GitHub Pages publica a branch main revisada; um fluxo de trabalho diário atualiza os registros dos badges e gera o site novamente. As verificações de PRs externas têm permissões somente de leitura.

Os dados de origem e os registros de revisão ficam neste repositório. O código-fonte dos harnesses e os recursos de seus lançamentos ficam nos respectivos repositórios. Nenhum vídeo, dependência ou registro privado de desenvolvimento de harnesses é instalado com o framework do Harneloop.
