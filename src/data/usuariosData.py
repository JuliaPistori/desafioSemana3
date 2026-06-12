import uuid
data_usuario= {
        "nome": "Nome Generico da Silva",
        "email": f"teste_{uuid.uuid4()}@email.com.br",
        "password": "123456A@",
        "administrador": "false"
}

data_usuario_2 = {
        "nome": "Outro Usuario",
        "email": f"teste_{uuid.uuid4()}@email.com",
        "password": "123456A@",
        "administrador": "false"
    }

usuario_admin = {"nome": "Administrador",
            "email": f"admin_{uuid.uuid4()}@email.com",
            "password": "123456A@",
            "administrador": "true"
            }