import pytest
import requests

from src.api.base import ENDPOINT_CARRINHOS
from src.api.base import ENDPOINT_PRODUTOS
from src.api.base import ENDPOINT_USUARIOS
from src.data.usuariosData import data_usuario, data_usuario_2


def test_listar_usuarios_retorna_estrutura_esperada_e_status_200():

    response = requests.get(ENDPOINT_USUARIOS)

    assert response.status_code == 200
    body = response.json()
    assert isinstance(body["usuarios"], list)
    assert body["quantidade"] 
    assert "usuarios" in body

def test_listar_usuarios_com_filtro_de_email_retorna_estrutura_esperada_e_status_200(usuario_teste):

    response = requests.get(ENDPOINT_USUARIOS, params={"email": usuario_teste["email"]})

    assert response.status_code == 200
    body = response.json()
    assert isinstance(body["usuarios"], list)
    assert body["quantidade"] == 1
    assert body["usuarios"][0]["email"] == usuario_teste["email"]

def test_cadastrar_usuario_com_sucesso_retorna_estrutura_esperada_e_status_201():

    response = requests.post(ENDPOINT_USUARIOS, json=data_usuario())

    assert response.status_code == 201
    body = response.json()
    assert "message" in body
    assert "_id" in body

    id_usuario = body["_id"]
    requests.delete(f"{ENDPOINT_USUARIOS}/{id_usuario}")

def test_cadastrar_usuario_com_email_ja_cadastrado_retorna_estrutura_esperada_e_status_400(usuario_teste):

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
    requests.delete(f"{ENDPOINT_USUARIOS}/{usuario_teste['id']}")

    response = requests.get(f"{ENDPOINT_USUARIOS}/{usuario_teste['id']}")
    assert response.status_code == 400
    body = response.json()
    assert "message" in body

def test_excluir_usuario_com_sucesso_retorna_estrutura_esperada_e_status_200(usuario_teste):

    response = requests.delete(f"{ENDPOINT_USUARIOS}/{usuario_teste['id']}")

    assert response.status_code == 200
    body = response.json()
    assert "message" in body

def test_excluir_usuario_nenhum_registro_excluido_retorna_estrutura_esperada_e_status_200():

    response = requests.delete(f"{ENDPOINT_USUARIOS}/0")

    assert response.status_code == 200
    body = response.json()
    assert "message" in body

def test_excluir_usuario_com_carrinho_cadastrado_retorna_estrutura_esperada_e_status_400(usuario_teste, carrinho_teste):

    response = requests.delete(f"{ENDPOINT_USUARIOS}/{carrinho_teste['id_usuario_carrinho']}")

    assert response.status_code == 400
    body = response.json()
    assert "message" in body
    assert "idCarrinho" in body

def test_editar_usuario_com_id_informado_encontrado_retorna_estrutura_esperada_e_status_200(usuario_teste):

    response = requests.put(f"{ENDPOINT_USUARIOS}/{usuario_teste['id']}", json=data_usuario())

    assert response.status_code == 200
    body = response.json()
    assert "message" in body

def test_editar_usuario_com_id_informado_nao_encontrado_retorna_estrutura_esperada_e_status_201(usuario_teste):

    requests.delete(f"{ENDPOINT_USUARIOS}/{usuario_teste['id']}")
    response = requests.put(f"{ENDPOINT_USUARIOS}/{usuario_teste['id']}", json=data_usuario())

    assert response.status_code == 201
    body = response.json()
    assert "message" in body
    assert "_id" in body

    id_nao_informado = body["_id"]
    requests.delete(f"{ENDPOINT_USUARIOS}/{id_nao_informado}")

def test_editar_usuario_com_email_ja_cadastrado_retorna_estrutura_esperada_e_status_400(usuario_teste):

    usuario_email_cadastrado = requests.post(ENDPOINT_USUARIOS, json=data_usuario())
    id_email_cadastrado = usuario_email_cadastrado.json()["_id"]
    response = requests.put(f"{ENDPOINT_USUARIOS}/{id_email_cadastrado}", json=usuario_teste["data"])

    assert response.status_code == 400
    body = response.json()
    assert "message" in body

    requests.delete(f"{ENDPOINT_USUARIOS}/{id_email_cadastrado}")
