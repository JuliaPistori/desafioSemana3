import pytest
import requests
import uuid




from src.api.base import ENDPOINT_CARRINHOS
from src.api.base import ENDPOINT_PRODUTOS
from src.api.base import ENDPOINT_USUARIOS
from src.api.base import ENDPOINT_LOGIN

from src.data.usuariosData import data_usuario
from src.data.usuariosData import usuario_admin
from src.data.produtosData import produto



@pytest.fixture
def usuario_teste():
    email = f"teste_{uuid.uuid4()}@email.com.br"

    data = {"nome": "Nome Generico da Silva",
            "email": email,
            "password": "123456A@",
            "administrador": "false"
            }


    response = requests.post(ENDPOINT_USUARIOS, json=data)
    assert response.status_code == 201

    id_usuario = response.json()["_id"]

    yield {
        "id": id_usuario,
        "data": data,
        "email": email,
    }

    requests.delete(f"{ENDPOINT_USUARIOS}/{id_usuario}")

@pytest.fixture
def carrinho_teste():

    data_admin = usuario_admin()
    admin = requests.post(ENDPOINT_USUARIOS, json=data_admin)
    id_admin = admin.json()["_id"]
    email = data_admin["email"]
    password = data_admin["password"]
    loginAdmin = requests.post(ENDPOINT_LOGIN, json={"email": email, "password": password})
    tokenAdmin = loginAdmin.json()["authorization"]
    headersAdmin = {"Authorization": tokenAdmin}

    produto_teste = requests.post(ENDPOINT_PRODUTOS, json=produto(), headers=headersAdmin)
    id_produto = produto_teste.json()["_id"]
    carrinho= {
  "produtos": [
    {
      "idProduto": id_produto,
      "quantidade": 1
    }
  ]
}
    data_usuario_carrinho = data_usuario()
    usuario_carrinho = requests.post(ENDPOINT_USUARIOS, json=data_usuario_carrinho)
    id_usuario_carrinho = usuario_carrinho.json()["_id"]
    email_carrinho = data_usuario_carrinho["email"]
    password_carrinho = data_usuario_carrinho["password"]
    loginCarrinho = requests.post(ENDPOINT_LOGIN, json={"email":email_carrinho, "password":password_carrinho})
    tokenCarrinho = loginCarrinho.json()["authorization"]
    headersCarrinho = {"Authorization": tokenCarrinho}
    response = requests.post(ENDPOINT_CARRINHOS, json=carrinho, headers=headersCarrinho)
    id_carrinho = response.json()["_id"]

    yield {
        "carrinho_id": id_carrinho,
        "id_usuario_carrinho": id_usuario_carrinho
    }

    requests.delete(f"{ENDPOINT_PRODUTOS}/{id_produto}")
    requests.delete(f"{ENDPOINT_CARRINHOS}/{id_carrinho}")
    requests.delete(f"{ENDPOINT_USUARIOS}/{id_admin}")
    requests.delete(f"{ENDPOINT_USUARIOS}/{id_usuario_carrinho}")