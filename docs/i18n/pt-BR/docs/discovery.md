# Descoberta e indexação

Endereços atuais desde `2026-10-20`: [OpenRootdev/harness-library](https://github.com/OpenRootdev/harness-library) e o [diretório](https://openrootdev.github.io/harness-library/). As notas históricas abaixo descrevem a mudança anterior.

O diretório público publica HTML completo em URLs estáveis. Mecanismos de busca, navegadores com JavaScript desativado e agentes podem ler diretamente a instalação, os pré-requisitos, a origem, a distribuição e o escopo de revisão de cada harness aprovado. JavaScript apenas melhora a filtragem, a cópia e a navegação antiga por fragmentos de URL.

## Recursos públicos

- [Diretório](https://openrootdev.github.io/harness-library/) e [guia de envio](https://openrootdev.github.io/harness-library/submit/).
- [Sitemap](https://openrootdev.github.io/harness-library/sitemap.xml): apenas páginas HTML canônicas. As verificações diárias de badges não inventam datas de modificação do conteúdo.
- [llms.txt](https://openrootdev.github.io/harness-library/llms.txt): um guia compacto com links para páginas de instalação em Markdown e dados.
- [llms-full.txt](https://openrootdev.github.io/harness-library/llms-full.txt): texto público combinado.
- [catalog.json](https://openrootdev.github.io/harness-library/catalog.json): entradas revisadas, URLs canônicas de páginas, instalação, configuração manual e evidências com escopo definido.
- Cada página HTML canônica tem um `index.md` correspondente, vinculado com `rel="alternate" type="text/markdown"`.

Cada página HTML tem título, descrição e URL canônica exclusivos, metadados de prévia social e JSON-LD correspondente. Os dados estruturados descrevem o diretório, o mantenedor e os harnesses reais; não inventam avaliações, downloads ou compatibilidade universal. Caminhos desconhecidos retornam o status 404 do GitHub Pages usando a página de erro noindex. Links antigos de entradas com fragmentos continuam compatíveis.

## Configuração do proprietário

1. Adicione uma **propriedade de prefixo de URL** para `https://openrootdev.github.io/harness-library/` no [Google Search Console](https://search.google.com/search-console). Isso limita a propriedade ao projeto. Use o método de verificação fornecido para sua conta; um arquivo HTML de verificação pode ser colocado em `site/` quando seu nome e conteúdo exatos forem fornecidos.
2. Envie `sitemap.xml` nessa propriedade. Inspecione as URLs da página inicial, do guia de envio e dos harnesses; solicite indexação quando a ferramenta oferecer essa opção. Um envio é uma indicação para descoberta, não uma promessa de indexação.
3. Adicione o mesmo site ao [Bing Webmaster Tools](https://www.bing.com/webmasters/) e envie o sitemap. Se a conta oferecer importação do Google Search Console, a propriedade verificada poderá ser reutilizada.
4. Consulte novamente os relatórios de indexação após a implantação. Corrija problemas de rastreamento ou conteúdo com base em evidências. Não trate uma busca `site:` ou uma pontuação do Lighthouse como prova de cobertura de indexação ou posicionamento.

A verificação exige a conta do proprietário ou o artefato de verificação fornecido por ela. Não publique tokens de verificação presumidos. Se um arquivo HTML de verificação for adicionado, mantenha-o fora do sitemap e preserve-o nas gerações.

## Notificações de alterações publicadas

Depois que um push normal é implantado, o fluxo de trabalho do Pages notifica o [IndexNow](https://www.indexnow.org/documentation) com as URLs canônicas do sitemap gerado. As atualizações diárias de badges ignoram essa notificação. Esta migração altera todas as cinco páginas; para um diretório maior, limite os envios às páginas alteradas. O Google usa Search Console e rastreamento comum; não são feitos envios ao Google pelo IndexNow.

O projeto hospeda `indexnow-key.txt` e fornece seu `keyLocation` exato. Isso limita a propriedade a `/harness-library/`, evitando projetos sem relação no host compartilhado. A chave precisa ser servida publicamente para a verificação do protocolo; ela não é uma credencial de conta de webmaster. Não é necessário login, serviço pago ou dependência adicional. Uma falha temporária da API não reverte uma implantação bem-sucedida do site.

Para uma atualização intencional de conteúdo fora do fluxo de trabalho, gere primeiro o site e execute `python scripts/notify_indexnow.py --dry-run` para inspecionar a lista de URLs, ou `python scripts/notify_indexnow.py` para enviá-la. HTTP 200 significa recebido; HTTP 202 significa recebido com validação da chave pendente. Nenhum dos dois comprova indexação ou posicionamento. Evite envios repetidos quando o conteúdo não mudou.

## GitHub Pages e robots.txt

As regras de robots são lidas na **raiz do host**, `https://openrootdev.github.io/robots.txt`, e não em `/harness-library/robots.txt`. Um arquivo local do projeto não controla o rastreamento do host compartilhado. O arquivo do projeto apenas indica o sitemap atual. Envie o sitemap pelas contas de webmaster.

Se o proprietário adicionar depois um repositório do site raiz ou um domínio personalizado, confira o arquivo robots autoritativo antes de implantar restrições. Nunca altere levianamente as regras de outros projetos no mesmo host.

## Migração para a organização

O repositório e o diretório foram transferidos para [Kaelux Labs](https://github.com/OpenRootdev/harness-library) em 10 de outubro de 2026. O GitHub redireciona a URL antiga do repositório. Um pequeno [repositório Pages da conta](https://github.com/Ker102/ker102.github.io) preserva as páginas antigas do diretório com redirecionamentos instantâneos e links canônicos, e continua servindo as imagens dos badges existentes. Seu `robots.txt` na raiz do host permite o rastreamento e inclui um link para o sitemap atual.

Links de retorno de badges que usem a URL antiga ou a atual do diretório continuam elegíveis. Alterar esses links não reinicia um destaque existente de 14 dias; as datas do registro original continuam autoritativas.

## Descoberta por agentes

Agentes podem usar HTML comum, o catálogo JSON ou espelhos Markdown. `llms.txt` é uma proposta de conveniência, não um fator de posicionamento do Google nem uma exigência. O Google afirma que seus recursos de busca com IA usam as mesmas práticas fundamentais de SEO da busca comum. Texto rastreável, links claros de páginas, evidências precisas e conteúdo útil importam; nenhuma configuração garante inclusão ou citações.

Referências primárias: [Google JavaScript SEO](https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics), [sitemaps](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap), [especificação de robots](https://developers.google.com/crawling/docs/robots-txt/robots-txt-spec), [recursos de IA](https://developers.google.com/search/docs/appearance/ai-features), [proposta llms.txt](https://llmstxt.org/).
