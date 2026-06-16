import pytest
import requests

from src.api.base import ENDPOINT_CARRINHOS
from src.api.base import ENDPOINT_PRODUTOS
from src.api.base import ENDPOINT_USUARIOS
from jsonschema import validate
from src.schemas.produto_schema import produto_schema
from src.data.usuariosData import data_usuario
from src.data.produtosData import produto

def test_listar_produtos_retorna_estrutura_esperada_e_status_200():
    response = requests.get(ENDPOINT_PRODUTOS)

    assert response.status_code == 200
    body = response.json()
    assert "quantidade" in body
    assert "produtos" in body

def test_listar_produtos_com_filtro_nome_retorna_estrutura_esperada_e_status_200(produto_teste):
    response = requests.get(ENDPOINT_PRODUTOS, params={"nome": produto_teste["dados_produto"]["nome"]})

    assert response.status_code == 200
    body = response.json()
    assert "quantidade" in body
    assert "produtos" in body

def test_listar_produtos_com_filtro_preco_retorna_estrutura_esperada_e_status_200(produto_teste):
    response = requests.get(ENDPOINT_PRODUTOS, params={"preco": produto_teste["dados_produto"]["preco"]})

    assert response.status_code == 200
    body = response.json()
    assert "quantidade" in body
    assert "produtos" in body

def test_cadastrar_produto_com_sucesso_retorna_estrutura_esperada_e_status_201(token_Admin_teste):

    response = requests.post(ENDPOINT_PRODUTOS,json= produto(), headers=token_Admin_teste["headers"] )

    assert response.status_code == 201
    body = response.json()
    assert "message" in body
    assert "_id" in body

    requests.delete(f"{ENDPOINT_PRODUTOS}/{body['_id']}")

def test_cadastrar_produto_com_nome_vazio_retorna_status_400(token_Admin_teste):

    response = requests.post(ENDPOINT_PRODUTOS,json={
        "nome": "",
        "preco": 70,
        "descricao": "Bem generico",
        "quantidade": 265
    } , headers=token_Admin_teste["headers"] )

    assert response.status_code == 400

def test_cadastrar_produto_sem_token_retorna_estrutura_esperada_e_status_401(token_Admin_teste):

    response = requests.post(ENDPOINT_PRODUTOS,json= produto(), headers= None)

    assert response.status_code == 401
    body = response.json()
    assert "message" in body

def test_cadastrar_produto_com_nome_ja_cadastrado_retorna_estrutura_esperada_e_status_400(token_Admin_teste, produto_teste):

    response = requests.post(ENDPOINT_PRODUTOS,json= produto_teste["dados_produto"], headers=token_Admin_teste["headers"] )

    assert response.status_code ==400
    body = response.json()
    assert "message" in body

def test_cadastrar_produto_com_usuario_nao_administrador_retorna_estrutura_esperada_e_status_403(token_User_teste):
    response = requests.post(ENDPOINT_PRODUTOS,json= produto(), headers=token_User_teste["headers"])

    assert response.status_code ==403
    body = response.json()
    assert "message" in body

def test_buscar_produto_com_id_encontrado_retorna_estrutura_esperada_e_status_200(produto_teste):
    response = requests.get(f"{ENDPOINT_PRODUTOS}/{produto_teste['id_produto']}")

    assert response.status_code == 200
    validate(instance=response.json(), schema=produto_schema)
    body = response.json()
    assert "nome" in body
    assert "preco" in body
    assert "descricao" in body
    assert "quantidade" in body
    assert "_id" in body

def test_buscar_produto_com_id_nao_encontrado_retorna_estrutura_esperada_e_status_400(produto_teste):
    response = requests.get(f"{ENDPOINT_PRODUTOS}/0000000000000000")

    assert response.status_code == 400
    body = response.json()
    assert "message" in body

def test_excluir_produto_com_sucessso_retorna_estrutura_esperada_e_status_200(token_Admin_teste, produto_teste):
    response = requests.delete(f"{ENDPOINT_PRODUTOS}/{produto_teste['id_produto']}", headers=token_Admin_teste["headers"])

    assert response.status_code == 200
    body = response.json()
    assert "message" in body

def test_excluir_produto_inexistente_retorna_estrutura_esperada_e_status_200(token_Admin_teste):
    response = requests.delete(f"{ENDPOINT_PRODUTOS}/0000000000000000", headers=token_Admin_teste["headers"])

    assert response.status_code == 200
    body = response.json()
    assert "message" in body

def test_excluir_produto_sem_token_retorna_estrutura_esperada_e_status_401(produto_teste):
    response = requests.delete(f"{ENDPOINT_PRODUTOS}/{produto_teste['id_produto']}",)

    assert response.status_code == 401
    body = response.json()
    assert "message" in body

def test_excluir_produto_com_usuario_nao_administrador_retorna_estrutura_esperada_e_status_403(token_User_teste, produto_teste):
    response = requests.delete(f"{ENDPOINT_PRODUTOS}/{produto_teste['id_produto']}", headers=token_User_teste["headers"])

    assert response.status_code == 403
    body = response.json()
    assert "message" in body

def test_excluir_produto_presente_em_carrinho_retorna_estrutura_esperada_e_status_400(token_Admin_teste, carrinho_teste):
    response = requests.delete(f"{ENDPOINT_PRODUTOS}/{carrinho_teste['id_produto']}", headers=token_Admin_teste["headers"])
    assert response.status_code == 400
    body = response.json()
    assert "message" in body
    assert "idCarrinhos" in body

def test_editar_produto_com_sucesso_retorna_estrutura_esperada_e_status_200(produto_teste, token_Admin_teste):
    response = requests.put(f"{ENDPOINT_PRODUTOS}/{produto_teste['id_produto']}", json= produto(), headers=token_Admin_teste["headers"])

    assert response.status_code == 200
    body = response.json()
    assert "message" in body
    
def test_editar_produto_com_id_inesxistente_retorna_estrutura_esperada_e_status_201(produto_teste, token_Admin_teste):
    requests.delete(f"{ENDPOINT_PRODUTOS}/{produto_teste['id_produto']}",headers=token_Admin_teste["headers"])
    response = requests.put(f"{ENDPOINT_PRODUTOS}/{produto_teste['id_produto']}", json= produto(), headers=token_Admin_teste["headers"])

    assert response.status_code == 201
    body = response.json()
    assert "message" in body
    assert "_id" in body

def test_editar_produto_com_nome_ja_cadastrado_retorna_estrutura_esperada_e_status_400(produto_teste, token_Admin_teste):
    produto_copiar_nome = requests.post(ENDPOINT_PRODUTOS,json= produto(), headers=token_Admin_teste["headers"] )
    response = requests.put(f"{ENDPOINT_PRODUTOS}/{produto_copiar_nome.json()["_id"]}", json= produto_teste["dados_produto"] , headers=token_Admin_teste["headers"])

    assert response.status_code == 400
    body = response.json()
    assert "message" in body

def test_editar_produto_sem_token_de_administrador_retorna_estrutura_esperada_e_status_201(produto_teste, token_Admin_teste):
    response = requests.put(f"{ENDPOINT_PRODUTOS}/{produto_teste['id_produto']}", json= produto())

    assert response.status_code == 401
    body = response.json()
    assert "message" in body

def test_editar_produto_com_usuario_nao_administrador_retorna_estrutura_esperada_e_status_403(produto_teste, token_User_teste):
    response = requests.put(f"{ENDPOINT_PRODUTOS}/{produto_teste['id_produto']}", json= produto(), headers=token_User_teste["headers"])

    print(response.status_code)
    print(response.json())

    assert response.status_code == 403
    body = response.json()
    assert "message" in body