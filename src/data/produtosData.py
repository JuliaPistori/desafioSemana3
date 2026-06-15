import uuid


def produto():
    return {
        "nome": f"Produto_{uuid.uuid4()}",
        "preco": 70,
        "descricao": "Bem generico",
        "quantidade": 265
    }
