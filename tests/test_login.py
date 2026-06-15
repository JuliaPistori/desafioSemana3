import pytest
import requests

from src.api.base import ENDPOINT_LOGIN
from src.helpers.helpers_login import criar_email

def test_realizar_login_com_dados_validos_retorna_estrutura_esperada_e_status_200(usuario_teste):

    email_login = usuario_teste["data"]["email"]
    senha_login = usuario_teste["data"]["password"]
    response = requests.post(ENDPOINT_LOGIN, json = {"email": email_login, "password": senha_login})

    assert response.status_code == 200
    body = response.json()
    assert "message" in body
    assert "authorization" in body
    assert body["message"] == "Login realizado com sucesso"

def test_realizar_login_com_a_senha_incorreta_retorna_estrutura_esperada_e_status_401(usuario_teste):

    email_login = usuario_teste["data"]["email"]
    senha_login = usuario_teste["data"]["password"]
    response = requests.post(ENDPOINT_LOGIN, json= {"email": email_login, "password": "senha_errada"})

    assert response.status_code == 401
    body = response.json()
    assert "message" in body
    assert body["message"] == "Email e/ou senha inválidos"

def test_realizar_login_com_o_email_incorreto_retorna_estrutura_esperada_e_status_401(usuario_test):

    senha_login = usuario_teste["data"]["password"]
    response = requests.post(ENDPOINT_LOGIN, json= {"email": criar_email(), "password": senha_login})

    assert response.status_code == 401
    body = response.json()
    assert "message" in body
    assert body["message"] == "Email e/ou senha inválidos"

def test_realizar_login_com_campos_vazios_retorna_status_400():

    response = requests.post(ENDPOINT_LOGIN, json= {"email": None , "password": None})

    assert response.status_code == 400 

