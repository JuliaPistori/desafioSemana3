import pytest
import requests
import uuid




from src.api.base import ENDPOINT_CARRINHOS
from src.api.base import ENDPOINT_PRODUTOS
from src.api.base import ENDPOINT_USUARIOS

from src.data.usuariosData import data_usuario
from src.data.produtosData import produto
from src.api.usuarios_api import criar_token_admin
from src.api.usuarios_api import criar_token_user



@pytest.fixture
def usuario_teste():
    email = f"teste_{uuid.uuid4()}@email.com.br"

    data = {"nome": "Nome Generico da Silva",
            "email": email,
            "password": "123456A@",
            "administrador": "false"
            }


    response = requests.post(ENDPOINT_USUARIOS, json=data)
    id_usuario = response.json()["_id"]

    yield {
        "id": id_usuario,
        "data": data,
        "email": email,
    }

    requests.delete(f"{ENDPOINT_USUARIOS}/{id_usuario}")

@pytest.fixture
def carrinho_teste():

    admin_data = criar_token_admin()

    dados_produto = produto()

    produto_teste = requests.post(
    ENDPOINT_PRODUTOS,
    json=produto(),
    headers=admin_data["headers"]
)
    id_produto = produto_teste.json()["_id"]

    user_data = criar_token_user()

    carrinho= {
  "produtos": [
    {
      "idProduto": id_produto,
      "quantidade": 1
    }
  ]
}
    response = requests.post(
        ENDPOINT_CARRINHOS, json=carrinho, headers=user_data["headers"]
    )
    id_carrinho = response.json()["_id"]

    yield {
    "carrinho_id": id_carrinho,
    "id_usuario_carrinho": user_data["id_user"],
    "id_produto": id_produto,
    "dados_produto": dados_produto
}

    requests.delete(f"{ENDPOINT_PRODUTOS}/{id_produto}")
    requests.delete(f"{ENDPOINT_CARRINHOS}/{id_carrinho}")
    requests.delete(f"{ENDPOINT_USUARIOS}/{admin_data['id_admin']}")
    requests.delete(f"{ENDPOINT_USUARIOS}/{user_data['id_user']}")

@pytest.fixture
def produto_teste():

    admin_data = criar_token_admin()
    dados_produto = produto()

    response = requests.post(
        ENDPOINT_PRODUTOS,
        json=dados_produto,
        headers=admin_data["headers"]
    )

    id_produto = response.json()["_id"]

    yield {
        "id_produto": id_produto,
        "dados_produto": dados_produto
    }

    requests.delete(f"{ENDPOINT_PRODUTOS}/{id_produto}")
    requests.delete(f"{ENDPOINT_USUARIOS}/{admin_data['id_admin']}")

@pytest.fixture
def token_Admin_teste():

    admin_data = criar_token_admin()

    yield admin_data

    requests.delete(
        f"{ENDPOINT_USUARIOS}/{admin_data['id_admin']}"
    )

@pytest.fixture
def token_User_teste():

    user_data = criar_token_user()

    yield user_data

    requests.delete(
        f"{ENDPOINT_USUARIOS}/{user_data['id_user']}"
    )

