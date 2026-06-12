import pytest
import requests

from src.api.base import ENDPOINT_CARRINHOS
from src.api.base import ENDPOINT_PRODUTOS
from src.api.base import ENDPOINT_USUARIOS
from src.data.usuariosData import data_usuario, data_usuario_2
from tests.conftest import usuario_teste


def test_listar_usuarios_retorna_estrutura_esperada_e_status_200():
    response = requests.get(ENDPOINT_USUARIOS)

    assert response.status_code == 200
    body = response.json()
    assert "quantidade" in body
    assert "usuarios" in body

    assert isinstance(body["usuarios"], list)

def test_cadastrar_usuario_com_sucesso_retorna_estrutura_esperada_e_status_201():
    response = requests.post(ENDPOINT_USUARIOS, json=data_usuario)
    assert response.status_code == 201

    body = response.json()

    assert "message" in body
    assert "_id" in body

    id_usuario = body["_id"]

    requests.delete(f"{ENDPOINT_USUARIOS}/{id_usuario}")

def test_cadastrar_usuario_com_email_ja_cadastrado_retorna_estrutura_esperada_e_status_400(usuario_teste):
    requests.post(ENDPOINT_USUARIOS, json=usuario_teste["data"])
    response = requests.post(ENDPOINT_USUARIOS, json=usuario_teste["data"])

    assert response.status_code == 400

    body = response.json()
    assert "message" in body

def test_buscar_usuario_por_id_usuario_encontrado_retorna_estrutura_esperada_e_status_200(usuario_teste):
    response = requests.get(f"{ENDPOINT_USUARIOS}/{usuario_teste['id']}")
    assert response.status_code == 200

    body = response.json()
    assert "nome" in body
    assert "email" in body
    assert "password" in body
    assert "administrador" in body
    assert "_id" in body

def test_buscar_usuario_por_id_usuario_nao_encontrado_retorna_estrutura_esperada_e_status_400(usuario_teste):
    requests.post(ENDPOINT_USUARIOS, json=usuario_teste["data"])
    id_apagado = usuario_teste["id"]
    requests.delete(f"{ENDPOINT_USUARIOS}/{id_apagado}")
    response = requests.get(f"{ENDPOINT_USUARIOS}/{id_apagado}")
    assert response.status_code == 400

    body = response.json()
    assert "message" in body

def test_excluir_usuario_com_sucesso_ou_nenhum_registro_excluido_retorna_estrutura_esperada_e_status_200(usuario_teste):
    requests.post(ENDPOINT_USUARIOS, json=usuario_teste["data"])
    response = requests.delete(f"{ENDPOINT_USUARIOS}/{usuario_teste["id"]}")

    assert response.status_code == 200
    body = response.json()
    assert "message" in body

def test_excluir_usuario_com_carrinho_cadastrado_retorna_estrutura_esperada_e_status_400(usuario_teste, carrinho_teste):
    requests.post(ENDPOINT_CARRINHOS, json=carrinho_teste)
    response = requests.delete(f"{ENDPOINT_USUARIOS}/{carrinho_teste['usuario_id']}")

    assert response.status_code == 400
    body = response.json()
    assert "message" in body
    assert "idCarrinho" in body

    requests.delete(f"{ENDPOINT_USUARIOS}/{carrinho_teste['usuario_id']}")

def test_editar_usuario_com_id_informado_encontrado_retorna_estrutura_esperada_e_status_200(usuario_teste):

    response = requests.put(
        f"{ENDPOINT_USUARIOS}/{usuario_teste['id']}",
        json=usuario_teste["data"]
    )

    assert response.status_code == 200
    body = response.json()
    assert "message" in body

def test_editar_usuario_com_id_informado_não_encontrado_retorna_estrutura_esperada_e_status_201(usuario_teste):
    requests.post(ENDPOINT_USUARIOS, json=usuario_teste["data"])
    id_apagado = usuario_teste["id"]
    requests.delete(f"{ENDPOINT_USUARIOS}/{id_apagado}")
    response = requests.put(f"{ENDPOINT_USUARIOS}/{id_apagado}", json=usuario_teste["data"])

    assert response.status_code == 201
    body = response.json()
    assert "message" in body
    assert "_id" in body

def test_editar_usuario_com_email_ja_cadastrado_retorna_estrutura_esperada_e_status_400(usuario_teste):
    requests.post(ENDPOINT_USUARIOS, json=usuario_teste["data"])
    usuario_id = requests.post(ENDPOINT_USUARIOS, json=data_usuario_2)
    id = usuario_id.json()["_id"]



    response = requests.put(f"{ENDPOINT_USUARIOS}/{id}", json=usuario_teste["data"])

    assert response.status_code == 400
    body = response.json()
    assert "message" in body