# Lista para envio

Um diretório aberto de skills, servidores MCP, CLIs, APIs, bibliotecas, plugins, fluxos e harnesses para agentes de IA. Cada entrada aponta diretamente para a fonte e explica configuração, licença ou termos e escopo da revisão.

## Contas e envios

Crie uma conta, confirme o e-mail e escolha um identificador. Personalize nome, biografia, site e avatar opcional. Você decide se o perfil será público e poderá ser indexado.

Salve um rascunho privado na interface e solicite revisão. Imagens são opcionais. Acompanhe status e comentários na conta. Somente versões aprovadas ficam públicas; alterações passam por nova revisão enquanto a versão aprovada anterior continua visível.

Conecte um agente ao endpoint MCP. No primeiro uso, o navegador abre login ou cadastro e uma tela explícita de permissões. O agente gerencia perfil, rascunhos e pedidos de revisão, mas não aprova nem publica envios.

[UI](https://toolindex.org/account/) · [MCP](https://toolindex.org/developers/) · [Guide](https://toolindex.org/submit/)

## Lista para envio

Descreva tarefa, fonte ou documentação oficial, tipo, categoria, versão, licença ou termos, instalação ou conexão, autenticação e custos. Nunca inclua segredos.

[JSON example](../../listing.example.json)

## Revisão e propriedade

Somente o proprietário edita ou retira um envio. Apenas um revisor verificado e configurado explicitamente pode publicar. As evidências públicas têm escopo limitado e não garantem todos os modelos ou plataformas. Rejeições e itens pendentes são privados.

## Contribuições ao código

A interface e MCP não exigem issue ou pull request. Contribuições ao código continuam bem-vindas. Entradas iniciais e registros de revisão e badges permanecem no controle de versão; não altere registros dos mantenedores ao enviar uma ferramenta.

```sh
python scripts/catalog.py validate
python -m unittest discover -s tests -v
python scripts/validate_i18n.py
npm ci --prefix backend
npm test --prefix backend
```

[README.md](README.md) · [Backend](../../../backend/README.md) · [Badge program](docs/badge-program.md)
