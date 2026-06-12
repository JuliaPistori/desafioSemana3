Automação de Testes de API - ServeRest






Visão geral do projeto

Este projeto consiste em uma suíte de testes automatizados de API utilizando Python, Pytest e Requests, aplicada à API pública ServeRest.

O objetivo é validar o comportamento dos endpoints de usuários e carrinhos, garantindo conformidade com regras de negócio, respostas esperadas e integridade dos dados.

Objetivos dos testes
Validar criação de usuários
Garantir regra de email único
Validar busca por ID
Testar edição de usuários
Validar exclusão com e sem dependências
Garantir regras de negócio de carrinho
Assegurar estrutura correta das respostas da API
Tecnologias utilizadas
Python 3.12+
Pytest
Requests
UUID (dados dinâmicos)
API ServeRest
API utilizada

ServeRest
https://compassuol.serverest.dev

Estrutura do projeto
desafioSemana3/
│
├── src/
│   ├── api/
│   │   └── base.py              # Endpoints da API
│   ├── data/
│   │   ├── usuariosData.py     # Massa de dados usuários
│   │   └── produtosData.py     # Massa de dados produtos
│
├── tests/
│   ├── conftest.py             # Fixtures (usuário, carrinho, admin)
│   └── test_usuarios.py        # Testes de usuários
│
└── README.md
Instalação do ambiente
1. Clonar o repositório
git clone <URL_DO_REPOSITORIO>
cd desafioSemana3
2. Criar ambiente virtual
python -m venv .venv
3. Ativar ambiente virtual

Windows:

.venv\Scripts\activate

Linux / Mac:

source .venv/bin/activate
4. Instalar dependências
pip install pytest requests
Execução dos testes

Executar todos os testes:

pytest

Executar com saída detalhada:

pytest -v

Executar com prints (debug):

pytest -v -s
Cobertura de testes
Usuários
Cadastro de usuário com sucesso
Cadastro com email duplicado
Busca por ID válido
Busca por ID inexistente
Edição de usuário com sucesso
Edição com email duplicado
Exclusão de usuário com sucesso
Exclusão de usuário com carrinho
Carrinho
Criação de carrinho com produto válido
Validação de usuário autenticado
Validação de produto existente
Remoção de carrinho e limpeza de dados
Estratégia de testes

Este projeto segue boas práticas de automação de API:

Dados dinâmicos com UUID para evitar conflitos
Uso de fixtures para setup e teardown
Testes independentes e isolados
Validação de status code e contrato da resposta
Uso de autenticação via token quando necessário
Limpeza automática de dados criados nos testes