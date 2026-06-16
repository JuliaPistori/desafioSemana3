import requests
from src.data.usuariosData import usuario_admin
from src.data.usuariosData import data_usuario
from src.api.base import ENDPOINT_USUARIOS
from src.api.base import ENDPOINT_LOGIN

def criar_token_admin():
    data_admin = usuario_admin()
    admin = requests.post(ENDPOINT_USUARIOS, json=data_admin)
    id_admin = admin.json()["_id"]
    email = data_admin["email"]
    password = data_admin["password"]
    loginAdmin = requests.post(ENDPOINT_LOGIN, json={"email": email, "password": password})
    token_admin = loginAdmin.json()["authorization"]

    return {
        "headers": {
            "Authorization": token_admin
        },
        "id_admin": id_admin
    }

def criar_token_user():
    data_user = data_usuario()
    user = requests.post(ENDPOINT_USUARIOS, json=data_user)
    id_user = user.json()["_id"]
    email = data_user["email"]
    password = data_user["password"]
    loginUser = requests.post(ENDPOINT_LOGIN, json={"email": email, "password": password})
    token_user = loginUser.json()["authorization"]

    return {
        "headers": {
            "Authorization": token_user
        },
        "id_user": id_user
    }
