import uuid


def data_usuario():
    return {
        "nome": "Nome Generico da Silva",
        "email": f"teste_{uuid.uuid4()}@email.com.br",
        "password": "123456A@",
        "administrador": "false"
    }


def data_usuario_senha_vazia():
    return {
        "nome": "Outro Usuario",
        "email": f"teste_{uuid.uuid4()}@email.com",
        "password": "",
        "administrador": "false"
    }


def data_usuario_nome_vazio():
    return {
        "nome": "",
        "email": f"teste_{uuid.uuid4()}@email.com",
        "password": "123456A@",
        "administrador": "false"
    }


def data_usuario_nome_invalido():
    return {
        "nome": "@!#$",
        "email": f"teste_{uuid.uuid4()}@email.com",
        "password": "123456A@",
        "administrador": "false"
    }


def data_usuario_email_vazio():
    return {
        "nome": "Outro Usuario",
        "email": "",
        "password": "123456A@",
        "administrador": "false"
    }


def usuario_admin():
    return {
        "nome": "Administrador",
        "email": f"admin_{uuid.uuid4()}@email.com",
        "password": "123456A@",
        "administrador": "true"
    }


def email_invalido():
    return f"errado_{uuid.uuid4()}@email.com"
