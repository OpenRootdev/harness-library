<p align="center"><img src="../../../site/assets/mark.svg" width="70" alt="ToolIndex"></p>
<h1 align="center">ToolIndex</h1>
<p align="center"><a href="../../../README.md">English</a> · <a href="../es/README.md">Español</a> · <a href="../zh-CN/README.md">简体中文</a> · <a href="../fr/README.md">Français</a> · <a href="../ja/README.md">日本語</a> · <a href="../de/README.md">Deutsch</a> · <a href="../pt-BR/README.md">Português (Brasil)</a></p>
<p align="center">Ferramentas para agentes de IA. Configuração clara. Links diretos para a origem.</p>
<p align="center"><a href="https://toolindex.org/">toolindex.org</a> · <a href="https://github.com/OpenRootdev/toolindex/issues/new?template=submit-tool.yml">Enviar uma ferramenta</a></p>

O ToolIndex é um diretório aberto de skills, servidores MCP, CLIs, APIs, bibliotecas, plugins, fluxos de trabalho e harnesses que agentes de IA podem usar. Pacotes locais, serviços hospedados e ferramentas comerciais são aceitos quando acesso, preços e termos estão claros.

## O que pode entrar

Ferramentas úteis para uma tarefa específica, de uma pequena pasta de skills a uma API. Cada listagem aponta diretamente para o repositório de origem ou a documentação oficial e explica instalação ou conexão, configuração manual, licença ou termos, versão e escopo da revisão.

## Enviar uma ferramenta

1. Abra o formulário do GitHub com nome, tipo, origem e finalidade da ferramenta.
2. Descreva o pacote ou serviço, instalação ou acesso, versão, licença ou termos, credenciais necessárias e custos. Nunca envie segredos.
3. O logotipo ou uma imagem personalizada são opcionais. Se houver imagem, informe URL, fonte e texto alternativo; caso contrário, são exibidas iniciais neutras.
4. Os mantenedores revisam e publicam as propostas aprovadas. Não é necessário fork, pull request ou conta do ToolIndex; o formulário requer uma conta do GitHub.

[CONTRIBUTING.md](CONTRIBUTING.md) · [JSON](../../../docs/listing.example.json)

## Exemplos revisados

Uma skill de animação de marca e um conector MCP para Blender demonstram dois tipos aceitos. O código e as versões continuam nos próprios repositórios.

- [Smooth Motion Graphics](https://toolindex.org/tools/smooth-motion-graphics/)
- [ViperMesh for Blender](https://toolindex.org/tools/vipermesh-blender/)

## Compilar e visualizar

Python 3.11+ gera o site estático. A interface usa HTML, CSS e JavaScript; a busca melhora páginas que continuam legíveis sem JavaScript.

```sh
python scripts/catalog.py validate
python -m unittest discover -s tests -v
python scripts/catalog.py build
python -m http.server 4201 --directory dist
```

`http://localhost:4201/`

## Hospedagem no Google Cloud

O Cloud Run serve o site com mínimo de 0 instâncias, máximo de 2 e cobrança por solicitação. O Firebase Hosting cuida do HTTPS do domínio e encaminha solicitações ao Cloud Run. A preparação do contexto público exclui arquivos privados do workspace. A ativação do domínio depende do DNS e do certificado.

`python scripts/stage_cloudrun.py` · [`firebase.json`](../../../firebase.json) · [docs/discovery.md](docs/discovery.md)

## Revisões e selos comunitários

As revisões de configuração e artefatos descrevem evidências específicas, não compatibilidade universal. Um selo opcional permite um destaque comunitário transparente de 14 dias. A atribuição ao Harneloop é opcional; nenhum framework é obrigatório.

[docs/badge-program.md](docs/badge-program.md)
