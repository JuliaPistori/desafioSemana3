# 🚀 Automação de Testes de API - ServeRest

Projeto de automação de testes voltado para a validação dos endpoints e regras de negócio da API pública ServeRest. A suíte cobre os fluxos principais de usuários, produtos e carrinhos, garantindo a integridade dos dados e a conformidade dos contratos da API.

---

## 🌐 API Utilizada

* **ServeRest:** [https://serverest.dev](https://serverest.dev)

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.12+** — Linguagem base do projeto.
* **Pytest** — Framework de testes e gerenciamento de fixtures.
* **Requests** — Biblioteca HTTP para requisições na API.
* **UUID** — Geração de dados dinâmicos e únicos.

---

## 📐 Estrutura do Projeto

```text
desafioSemana3/
│
├── src/
│   ├── api/
│   │   └── base.py              # Centralização dos endpoints da API
│   └── data/
│       ├── usuariosData.py      # Massa de dados de usuários
│       └── produtosData.py      # Massa de dados de produtos
│
├── tests/
│   ├── conftest.py              # Fixtures reutilizáveis (user, carrinho, admin, autenticação)
│   └── test_usuarios.py         # Casos de teste da API de usuários
│
└── README.md
```

---

## 🧪 Cobertura de Cenários (Test Cases)

### 📋 Casos de Teste Detalhados

#### Caso 01 - Cadastro de usuário com sucesso
* **Cenário:** Usuário cria conta com dados válidos.
* **Resultado esperado:** Status code `201` e retorno do campo `_id`.

#### Caso 02 - Cadastro com email duplicado
* **Cenário:** Usuário tenta cadastrar email já existente.
* **Resultado esperado:** Status code `400` e mensagem de erro explicativa.

#### Caso 03 - Buscar usuário por ID existente
* **Cenário:** Consulta de usuário válido no banco de dados.
* **Resultado esperado:** Status code `200` e retorno com os dados do usuário.

#### Caso 04 - Buscar usuário por ID inexistente
* **Cenário:** Consulta de ID de usuário removido ou inválido.
* **Resultado esperado:** Status code `400` e mensagem de erro correspondente.

#### Caso 05 - Exclusão de usuário com sucesso
* **Cenário:** Usuário sem dependências no sistema é removido.
* **Resultado esperado:** Status code `200` e mensagem de sucesso.

#### Caso 06 - Exclusão de usuário com carrinho cadastrado
* **Cenário:** Usuário com carrinho ativo tenta ser excluído do sistema.
* **Resultado esperado:** Status code `400` e retorno do `idCarrinho` vinculado.

#### Caso 07 - Edição de usuário com sucesso
* **Cenário:** Atualização de dados cadastrais de um usuário válido.
* **Resultado esperado:** Status code `200` e mensagem de sucesso.

#### Caso 08 - Edição com ID inexistente
* **Cenário:** Atualização de dados de um usuário removido ou ID inválido.
* **Resultado esperado:** Status code `201` (criação automática conforme comportamento nativo da API).

#### Caso 09 - Edição com email já cadastrado
* **Cenário:** Usuário tenta atualizar seus dados utilizando um email já existente no sistema.
* **Resultado esperado:** Status code `400` e mensagem de erro.

#### Caso 10 - Listagem de usuários
* **Cenário:** Consulta geral de registros de usuários cadastrados.
* **Resultado esperado:** Status code `200`, retorno da lista de usuários e contador de quantidade.


---

## 🎯 Estratégia de Testes e Boas Práticas

* **Separação de Responsabilidades:** Divisão clara entre chamadas de API (`src/api`), massas de dados (`src/data`) e testes (`tests`).
* **Isolamento Total:** Os testes são independentes e não possuem ordem de dependência mútua.
* **Dados Dinâmicos:** Uso de UUID para gerar e-mails e dados únicos a cada execução, evitando falsos negativos por dados duplicados.

---

## 👤 Autor

* **Julia Pistori** 
