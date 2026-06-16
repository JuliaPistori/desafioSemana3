# Plano de Testes – Evolução da Suíte ServeRest

## Objetivo

Evoluir a suíte automatizada da API ServeRest, garantindo a validação dos principais fluxos funcionais e regras de negócio dos endpoints priorizados, aumentando a confiança na aplicação e reduzindo o risco de regressões.

---

## Estratégia de Teste

Serão executados testes automatizados de API diretamente nos endpoints disponibilizados pela ServeRest.

A estratégia adotada contempla:

- validação de cenários positivos e negativos;
- verificação dos códigos de status HTTP;
- validação da estrutura das respostas;
- validação das principais regras de negócio descritas na documentação da API;
- utilização de fixtures para criação e limpeza de dados;
- independência entre os testes.

A priorização dos cenários foi baseada no impacto para o negócio, risco associado e prazo disponível para entrega.

---

## Escopo

### Em escopo nesta entrega

- Funcionalidades relacionadas aos endpoints de Usuários;
- Funcionalidades relacionadas ao endpoint de Login;
- Funcionalidades relacionadas aos endpoints de Produtos;
- Regras de autenticação e autorização;
- Tratamento dos principais cenários de erro previstos na documentação.

### Fora do escopo nesta entrega

Não serão contemplados:

- testes de performance;
- testes de carga;
- testes de segurança;
- testes de interface gráfica;
- testes de concorrência;
- validação de expiração do token de autenticação;
- automação de cenários classificados como baixa prioridade.

---

## Cenários Implementados

### Usuários

#### GET /usuarios

- Listar usuários com sucesso;
- Filtrar usuário por e-mail.

#### POST /usuarios

- Cadastrar usuário com sucesso;
- Impedir cadastro com e-mail já utilizado;
- Impedir cadastro com nome vazio;
- Impedir cadastro com e-mail vazio;
- Impedir cadastro com senha vazia;
- Validar comportamento com nome contendo caracteres especiais (BUG-001).

#### GET /usuarios/{id}

- Buscar usuário existente;
- Buscar usuário inexistente.

#### DELETE /usuarios/{id}

- Excluir usuário com sucesso;
- Tentar excluir usuário inexistente;
- Impedir exclusão de usuário com carrinho cadastrado.

#### PUT /usuarios/{id}

- Alterar usuário existente;
- Cadastrar usuário ao informar ID inexistente;
- Impedir alteração utilizando e-mail já cadastrado.

---

### Login

#### POST /login

- Realizar login com sucesso;
- Impedir login com senha inválida;
- Impedir login com e-mail inexistente;
- Impedir login com senha vazia;
- Impedir login com campos obrigatórios vazios.

---

### Produtos

#### GET /produtos

- Listar produtos com sucesso;
- Filtrar produto por nome;
- Filtrar produto por preço.

#### POST /produtos

- Cadastrar produto com usuário administrador;
- Impedir cadastro de produto com nome já utilizado;
- Impedir cadastro de produto com nome vazio;
- Impedir cadastro sem token de autenticação;
- Impedir cadastro utilizando usuário não administrador.

#### GET /produtos/{id}

- Buscar produto existente;
- Buscar produto inexistente.

#### DELETE /produtos/{id}

- Excluir produto com sucesso;
- Excluir produto inexistente;
- Impedir exclusão sem token de autenticação;
- Impedir exclusão utilizando usuário não administrador;
- Impedir exclusão de produto presente em carrinho.

#### PUT /produtos/{id}

- Alterar produto existente;
- Cadastrar produto ao informar ID inexistente;
- Impedir alteração utilizando nome já cadastrado;
- Impedir alteração sem token de autenticação;
- Impedir alteração utilizando usuário não administrador.

---

## Cenários Não Implementados

### Usuários

#### GET /usuarios com filtros

- Filtrar por nome;
- Filtrar por senha;
- Filtrar por ID;
- Filtrar usuários administradores.

---

### Produtos

#### GET /produtos com filtros

- Filtrar por descrição;
- Filtrar por quantidade;
- Filtrar por ID.

---

### Login

#### POST /login

- Validar comportamento com token expirado.

---

## Critérios de Qualidade

Um cenário será considerado concluído quando:

- executar com sucesso individualmente;
- executar com sucesso em conjunto com os demais testes;
- validar o código de status esperado;
- validar as informações relevantes da resposta;
- respeitar as regras de negócio previstas na documentação;
- não depender da ordem de execução dos testes;
- realizar a limpeza dos dados criados durante sua execução, quando aplicável.

---

## Considerações Finais

Este plano poderá ser atualizado conforme a evolução da suíte, identificação de novos riscos ou descoberta de comportamentos inesperados da API.

Durante a execução dos testes, eventuais defeitos identificados serão registrados formalmente como bug reports no repositório do projeto.

A suíte foi desenvolvida utilizando Python, Pytest e Requests, seguindo princípios de reutilização de código através de fixtures e funções auxiliares para autenticação e preparação de dados.