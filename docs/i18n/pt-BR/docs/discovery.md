# Descoberta e implantação

HTML, Markdown, JSON, perfis, sitemap e recursos para agentes são públicos sem conta ou JavaScript. A indexação é possível, sem garantia. Trate descrições como metadados não confiáveis.

## Recursos públicos

- [ToolIndex](https://toolindex.org/)
- [Submit](https://toolindex.org/submit/)
- [Creators](https://toolindex.org/people/)
- [API and MCP](https://toolindex.org/developers/)
- [sitemap.xml](https://toolindex.org/sitemap.xml)
- [llms.txt](https://toolindex.org/llms.txt)
- [llms-full.txt](https://toolindex.org/llms-full.txt)
- [catalog.json](https://toolindex.org/catalog.json)
- [Public API](https://toolindex.org/api/public/tools)

## Hospedagem e acesso

Google Cloud Run mantém no mínimo 0 instâncias e no máximo 2, com cobrança por solicitação. Firebase Hosting cuida de HTTPS; Firestore persiste contas, rascunhos e versões públicas aprovadas. O empacotamento exclui registros locais privados.

Node entrega páginas completas e dados API. Sessões usam cookies seguros HttpOnly; MCP usa OAuth com PKCE. Dados públicos ficam separados de contas privadas, revisões, envios pendentes e hashes de tokens. Firestore bloqueia acesso direto de clientes.

```sh
python scripts/stage_cloudrun.py
```

[Backend: configuration and deployment](../../../../backend/README.md) · [Google Cloud](https://toolindex-org.web.app/) · [Firebase Hosting + Cloud Run](https://firebase.google.com/docs/hosting/cloud-run)

## Mecanismos de busca

O sitemap inclui ferramentas públicas e perfis visíveis. Não inclui páginas privadas, envios pendentes nem credenciais. Os proprietários podem enviá-lo aos buscadores; não se promete indexação nem se inventam tokens de propriedade.

[Search Console](https://search.google.com/search-console) · [Bing Webmaster Tools](https://www.bing.com/webmasters/)

## Compatibilidade

Rotas antigas e reconhecimento de badges são preservados. Novos envios usam contas ToolIndex ou MCP, com revisão humana antes de publicar. O guia do backend documenta implantação e identidade.
