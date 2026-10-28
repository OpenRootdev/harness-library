# Listed in ToolIndex: destaque comunitário gratuito de 14 dias

O programa recompensa colaboradores que facilitam a descoberta de harnesses reutilizáveis. Não há pagamento nem obrigação de usar Harneloop.

1. Obtenha a aprovação da sua entrada.
2. Copie o trecho do badge da página de detalhes no diretório e coloque-o nas **primeiras 30 linhas** do README da branch padrão do repositório de origem.
3. Mantenha a imagem vinculada à sua entrada exata. A próxima execução de verificação concede um único **período de 14 dias**, iniciado na primeira verificação bem-sucedida em UTC.

Exemplo:

```md
[![Listed in ToolIndex](https://toolindex.org/badges/your-slug.svg)](https://toolindex.org/tools/your-slug/)
```

São aceitos o Markdown exato ou uma imagem HTML vinculada equivalente. O texto alternativo da imagem deve ser “Listed in ToolIndex”. Exemplos dentro de blocos de código ou comentários HTML não se qualificam.

Links de retorno emitidos anteriormente, `https://toolindex.org/#your-slug`, continuam válidos e levam à página correspondente. Use a URL real da página para novos badges.

Entradas ativas aparecem antes das entradas comuns e, dentro de cada grupo, em ordem alfabética. Os filtros de busca e categoria continuam aplicáveis. O diretório exibe o rótulo **Community boost** e sua expiração na página de detalhes. Isso é posicionamento promocional; o status de revisão e as afirmações de qualidade permanecem independentes.

O fluxo de trabalho diário da branch main confiável lê apenas metadados públicos dos READMEs no GitHub. Ele registra a concessão inicial, a expiração, a presença mais recente do badge e o horário da verificação em `data/boosts.json`. Não executa código de repositórios de harnesses. Remover o badge interrompe o destaque após a próxima verificação. Colocá-lo de volta pode restaurar apenas o restante do período original. Concessões expiradas nunca são renovadas automaticamente. Envios duplicados, mudanças de slug ou transferências de repositório não dão ao mesmo harness o direito a uma segunda recompensa inicial; os mantenedores verificam a identidade.

Se o GitHub ficar temporariamente indisponível, nenhum novo destaque será concedido. Badges já verificados continuam elegíveis por no máximo 48 horas sem uma nova verificação e nunca além da expiração original. Tanto a geração estática quanto o navegador verificam novamente os horários registrados. Os registros precisam de aprovação de um mantenedor; alterar um campo JSON em um envio não pode conceder um destaque.

O badge pode permanecer após a expiração. Uma nova política seria discutida publicamente; não há promoção recorrente oculta nem ranking pago.

Badges emitidos antes da migração para Kaelux Labs em `https://toolindex.org/` continuam válidos. A migração não reinicia a janela original de 14 dias. Atualize tanto a imagem quanto o link de retorno para o novo endereço canônico quando for conveniente.

O ToolIndex inclui qualquer ferramenta que agentes de IA possam usar: skills, servidores MCP, CLIs, APIs, bibliotecas, plugins, fluxos de trabalho e harnesses. Serviços hospedados e ferramentas comerciais são aceitos quando acesso, preços, autenticação e termos estão claros. Cada listagem aponta diretamente para o repositório de origem ou a documentação oficial.

O logotipo ou uma imagem personalizada são opcionais. Se houver imagem, informe a fonte e o texto alternativo; caso contrário, a listagem mostra iniciais neutras. Escolha o tipo de ferramenta e explique a instalação ou o acesso ao serviço. Fontes fora do GitHub são aceitas; a verificação automática de selos em README atualmente só funciona no GitHub.
