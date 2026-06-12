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

### Usuários
* **Cadastro:** Criação com sucesso e validação de bloqueio para e-mail duplicado.
* **Busca:** Consulta por ID válido e tratamento de erro para ID inexistente.
* **Edição:** Atualização de dados cadastrais e validação de conflito de e-mail duplicado.
* **Exclusão:** Remoção de usuário com sucesso e bloqueio de exclusão para usuários vinculados a carrinhos ativos.

### Carrinho
* **Criação:** Associação de produto válido ao carrinho de um usuário autenticado.
* **Regras de Negócio:** Validação de token de autenticação e existência prévia do produto.
* **Limpeza:** Remoção do carrinho e desvinculação dos dados pós-teste.

---

## 🎯 Estratégia de Testes e Boas Práticas

* **Separação de Responsabilidades:** Divisão clara entre chamadas de API (`src/api`), massas de dados (`src/data`) e testes (`tests`).
* **Isolamento Total:** Os testes são independentes e não possuem ordem de dependência mútua.
* **Dados Dinâmicos:** Uso de UUID para gerar e-mails e dados únicos a cada execução, evitando falsos negativos por dados duplicados.
* **Gerenciamento de Ciclo de Vida:** Uso de fixtures do Pytest para `setup` (preparação) e `teardown` (limpeza e deleção automática de dados gerados).
* **Validação Robusta:** Verificação simultânea de Status Code, regras de negócio e estrutura do contrato JSON.

---

## 🔮 Melhorias Futuras

* Implementação de pipeline de CI/CD via **GitHub Actions**.
* Geração de relatórios visuais utilizando **Allure Reports**.
* Refatoração para arquitetura de **Service Layer** dedicada por módulo.
* Separação de arquivos de teste por contexto (users, products, carts).
* Conteinerização do ambiente de testes utilizando **Docker**.

---

## 👤 Autor

* **Julia Pistori** — Engenharia de Qualidade e Automação de Testes de API com Python e Pytest.
