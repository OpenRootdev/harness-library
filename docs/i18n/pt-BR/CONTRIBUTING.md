# Envie um harness

O ToolIndex inclui qualquer ferramenta que agentes de IA possam usar: skills, servidores MCP, CLIs, APIs, bibliotecas, plugins, fluxos de trabalho e harnesses. Serviços hospedados e ferramentas comerciais são aceitos quando acesso, preços, autenticação e termos estão claros. Cada listagem aponta diretamente para o repositório de origem ou a documentação oficial.

O logotipo ou uma imagem personalizada são opcionais. Se houver imagem, informe a fonte e o texto alternativo; caso contrário, a listagem mostra iniciais neutras. Escolha o tipo de ferramenta e explique a instalação ou o acesso ao serviço. Fontes fora do GitHub são aceitas; a verificação automática de selos em README atualmente só funciona no GitHub.

**Novos envios são bem-vindos.** Procuramos configurações práticas e reutilizáveis para agentes, incluindo pequenas pastas de habilidades. Harneloop é opcional.

O caminho mais simples não exige fork nem pull request:

1. [Abra o formulário de envio no GitHub](https://github.com/OpenRootdev/toolindex/issues/new?template=submit-tool.yml). Informe o repositório, o nome e a tarefa/categoria.
2. Explique a instalação, a distribuição específica, a versão/licença e quaisquer conexões manuais. Detalhes adicionais de composição e evidências de testes são opcionais.
3. Os mantenedores revisam sua issue, pedem as informações faltantes nela se necessário e publicam as entradas aprovadas. Alterações posteriores podem ser enviadas em outra issue ou PR.

Você só precisa de uma conta do GitHub para usar o formulário. O [guia do site](https://toolindex.org/submit/) explica o mesmo processo.

Para uma PR, copie `docs/listing.example.json` para `data/listings/your-slug.json`. Use o mesmo slug em letras minúsculas no nome do arquivo e em `id`. Execute `python scripts/catalog.py validate` e os testes descritos no README.

Informações obrigatórias:

- Nome, resumo curto, categoria, repositório de origem, licença e versão ou revisão fixada.
- URL da distribuição específica, seu conteúdo e se o repositório de origem também contém material irrelevante. Use um pacote para download ou uma branch dedicada ao harness em repositórios mistos; não exija que os usuários clonem um projeto grande e sem relação com o objetivo.
- Instruções de instalação claras e ordenadas. Informe o diretório de trabalho, os pré-requisitos, a integração com agente/cliente e como começar. Inclua links para orientações específicas do cliente quando o mecanismo de descoberta for diferente.
- Conexões/configuração manuais, MCPs ou ferramentas obrigatórios, credenciais se houver e notas adicionais. Use listas vazias quando nada for necessário. Nunca envie segredos.

Opcional: contagens de habilidades/referências/arquivos, contagem de ferramentas MCP de nível superior, ferramentas de execução, composição detalhada e uma atribuição “Built with Harneloop” com evidências. Diferencie ferramentas opcionais das obrigatórias e ferramentas de despacho de nível superior das operações posteriores.

Categorias permitidas: Creative, 3D & Blender, Coding, Research, Data, Operations, Other. Sugira uma nova categoria na issue se nenhuma servir.

Não adicione campos de revisão ou destaque à entrada nem modifique os registros dos mantenedores. Os mantenedores controlam `data/reviews.json` e `data/boosts.json`. A atribuição de origem e as afirmações sobre testes precisam de evidências; um pacote lançado, por si só, não prova que funciona corretamente. Os mantenedores inspecionam instruções, escopo do código-fonte, licenças, URLs e artefatos declarados; scripts enviados nunca são executados automaticamente.

Mantenha as alterações focadas. Atualizações de pacotes de origem ou de passos de instalação devem incluir a versão e o que mudou. Instalações com problemas podem ser relatadas em uma issue comum.
