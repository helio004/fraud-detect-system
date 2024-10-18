responses = {
    200: {
        "description": "Resposta com a detecção de fraude",
        "content": {
            "application/json": {
                "example": {
                    "is_fraud": True,
                    "probability": 0.90
                }
            }
        },
    },
    404: {
        "description": "Erro ao carregar o modelo",
        "content": {
            "application/json": {
                "example": {
                    "detail": "Modelo não carregado e/ou não existente"
                }
            }
        },
    },
}
