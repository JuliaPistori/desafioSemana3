import uuid


def data_usuario():
    return {
        "nome": "Nome Generico da Silva",
        "email": f"teste_{uuid.uuid4()}@email.com.br",
        "password": "123456A@",
        "administrador": "false"
    }


def data_usuario_2():
    return {
        "nome": "Outro Usuario",
        "email": f"teste_{uuid.uuid4()}@email.com",
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
