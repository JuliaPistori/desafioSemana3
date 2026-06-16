# 🚀 Automação de Testes de API - ServeRest

Projeto de automação de testes desenvolvido para validação dos principais fluxos e regras de negócio da API pública ServeRest.

A suíte contempla testes automatizados dos endpoints de Usuários, Login e Produtos, cobrindo cenários positivos, negativos, autenticação, autorização e validações de regras de negócio.

---

## 🌐 API Utilizada

**ServeRest**

https://serverest.dev

---

## 🛠️ Tecnologias Utilizadas

- Python 3.13+
- Pytest
- Requests
- Pytest-Cov
- UUID
- Git
- GitHub

---

## 📐 Estrutura do Projeto

```text
desafioSemana3/
│
├── src/
│   ├── api/
│   │   ├── base.py
│   │   └── usuarios_api.py
│   │
│   ├── data/
│   │   ├── usuariosData.py
│   │   └── produtosData.py
│   │
│   └── helpers/
│       ├── auth.py
│       └── helpers_login.py
│
├── tests/
│   ├── conftest.py
│   ├── test_usuarios.py
│   ├── test_login.py
│   └── test_produtos.py
│
├── README.md
└── PLANO-DE-TESTES.md
```

---

## 🧪 Escopo da Automação

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
- Validar comportamento para nome com caracteres especiais (bug conhecido).

#### GET /usuarios/{id}

- Buscar usuário existente;
- Buscar usuário inexistente.

#### DELETE /usuarios/{id}

- Excluir usuário com sucesso;
- Excluir usuário inexistente;
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

## 🎯 Estratégia de Testes

A suíte foi construída seguindo os seguintes princípios:

- Independência entre os testes;
- Reutilização através de fixtures;
- Limpeza automática dos dados criados;
- Dados dinâmicos utilizando UUID;
- Validação de status codes HTTP;
- Validação da estrutura das respostas;
- Cobertura de cenários positivos e negativos;
- Cobertura das principais regras de negócio da API.

---

## 📊 Cobertura de Testes

### Método utilizado

A cobertura foi calculada utilizando o plugin **pytest-cov**, conforme a abordagem descrita no artigo:

https://medium.com/revista-dtar/como-verificar-a-cobertura-de-testes-da-api-rest-9e2f745564b

Comando utilizado:

```bash
pytest --cov=src --cov-report=term-missing
```

### Resultado obtido

```text
Name                           Stmts   Miss  Cover
--------------------------------------------------
src/api/base.py                    5      0   100%
src/api/usuarios_api.py           23      0   100%
src/data/produtosData.py           3      0   100%
src/data/usuariosData.py          13      0   100%
src/helpers/helpers_login.py       3      0   100%
--------------------------------------------------
TOTAL                             47      0   100%
```

### Cobertura total atingida

**100% de cobertura do código da suíte automatizada.**

Foram cobertas todas as linhas dos módulos avaliados pelo relatório de cobertura.

### Cenários fora do escopo

Apesar da cobertura total do código analisado, alguns cenários permaneceram fora do escopo desta entrega:

- Testes de performance;
- Testes de carga;
- Testes de segurança;
- Testes de concorrência;
- Validação da expiração de token;
- Alguns filtros secundários disponibilizados pela API.

A priorização foi realizada considerando risco, valor de negócio e prazo disponível para entrega.

---

## 🐞 Bug Identificado

### BUG-001 – Cadastro de usuário aceita caracteres especiais no nome

#### Descrição

Foi identificado que a API permite o cadastro de usuários contendo caracteres especiais no campo `nome`, comportamento considerado inconsistente com a regra de validação esperada para nomes de usuários.

#### Evidência

O cenário foi implementado utilizando:

```python
@pytest.mark.xfail(reason="BUG-001: API aceita caracteres especiais no nome")
```

permitindo registrar o comportamento observado sem comprometer a execução da suíte.

#### Severidade

Média.

---

## ▶️ Como Executar o Projeto

### 1. Clonar o repositório

```bash
git clone <url-do-repositorio>
```

### 2. Acessar a pasta do projeto

```bash
cd desafioSemana3
```

### 3. Criar ambiente virtual

```bash
python -m venv .venv
```

### 4. Ativar ambiente virtual

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 5. Instalar dependências

```bash
pip install -r requirements.txt
```

### 6. Executar todos os testes

```bash
pytest
```

### 7. Executar testes com relatório de cobertura

```bash
pytest --cov=src --cov-report=term-missing
```

---

## 📋 Resultados da Última Execução

```text
40 passed
1 xfailed
```

A suíte executou com sucesso todos os cenários implementados.

O cenário marcado como **xfail** corresponde ao bug conhecido documentado neste projeto.

---

## 📄 Documentação Complementar

- `PLANO-DE-TESTES.md` — Planejamento da estratégia de testes.
- `README.md` — Documentação técnica e instruções de execução.

---

## 👤 Autor

**Julia Pistori**