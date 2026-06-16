produto_schema = {
    "type": "object",
    "properties": {
        "nome": {"type": "string"},
        "preco": {"type": "number"},
        "descricao": {"type": "string"},
        "quantidade": {"type": "number"},
        "_id": {"type": "string"}
    },
    "required": [
        "nome",
        "preco",
        "descricao",
        "quantidade",
        "_id"
    ]
}