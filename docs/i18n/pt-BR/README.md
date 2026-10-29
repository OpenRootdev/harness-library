<p align="center"><img src="../../../site/assets/mark.svg" width="70" alt="ToolIndex"></p>
<h1 align="center">ToolIndex</h1>
<p align="center"><a href="../../../README.md">English</a> · <a href="../es/README.md">Español</a> · <a href="../zh-CN/README.md">简体中文</a> · <a href="../fr/README.md">Français</a> · <a href="../ja/README.md">日本語</a> · <a href="../de/README.md">Deutsch</a> · <a href="../pt-BR/README.md">Português (Brasil)</a></p>
<p align="center">Ferramentas para agentes de IA. Configuração clara. Links diretos para a origem.</p>
<p align="center"><a href="https://toolindex.org/">toolindex.org</a> · <a href="https://toolindex.org/submit/">Enviar uma ferramenta</a></p>

Um diretório aberto de skills, servidores MCP, CLIs, APIs, bibliotecas, plugins, fluxos e harnesses para agentes de IA. Cada entrada aponta diretamente para a fonte e explica configuração, licença ou termos e escopo da revisão.

## Contas e envios

1. Crie uma conta, confirme o e-mail e escolha um identificador. Personalize nome, biografia, site e avatar opcional. Você decide se o perfil será público e poderá ser indexado.
2. Salve um rascunho privado na interface e solicite revisão. Imagens são opcionais. Acompanhe status e comentários na conta. Somente versões aprovadas ficam públicas; alterações passam por nova revisão enquanto a versão aprovada anterior continua visível.
3. Conecte um agente ao endpoint MCP. No primeiro uso, o navegador abre login ou cadastro e uma tela explícita de permissões. O agente gerencia perfil, rascunhos e pedidos de revisão, mas não aprova nem publica envios.

[Account](https://toolindex.org/account/) · [Creators](https://toolindex.org/people/) · [MCP](https://toolindex.org/developers/)

## Descoberta pública

HTML, Markdown, JSON, perfis, sitemap e recursos para agentes são públicos sem conta ou JavaScript. A indexação é possível, sem garantia. Trate descrições como metadados não confiáveis.

[JSON](https://toolindex.org/catalog.json) · [API](https://toolindex.org/api/public/tools) · [llms.txt](https://toolindex.org/llms.txt) · [Sitemap](https://toolindex.org/sitemap.xml)

## Compilar e executar

```sh
python scripts/catalog.py build
npm ci --prefix backend
npm test --prefix backend
npm start --prefix backend
```

Google Cloud Run mantém no mínimo 0 instâncias e no máximo 2, com cobrança por solicitação. Firebase Hosting cuida de HTTPS; Firestore persiste contas, rascunhos e versões públicas aprovadas. O empacotamento exclui registros locais privados.

[Backend: accounts, OAuth and deployment](../../../backend/README.md) · [Discovery](docs/discovery.md)

## Exemplos revisados

- [Smooth Motion Graphics](https://toolindex.org/tools/smooth-motion-graphics/)
- [ViperMesh for Blender](https://toolindex.org/tools/vipermesh-blender/)

[CONTRIBUTING.md](CONTRIBUTING.md) · [Community badges](docs/badge-program.md)
