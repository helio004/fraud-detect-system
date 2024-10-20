from fastapi import APIRouter, HTTPException
from core.modelops import ModelLoader
from core.models import RequestModel, ResponseModel
from services.responses import responses


prediction_router = APIRouter(
    tags=["prediction-service"],
)

model_loader = ModelLoader(model_path="model")


@prediction_router.post(
    path='/fraud_detection/',
    response_model=ResponseModel,
    summary="Detecta Fraude em Transações",
    responses=responses
)
async def fraud_detection(features: RequestModel) -> ResponseModel:
    """
    Detecta se uma transação é fraudulenta com base nas características fornecidas.

    - **category**: A categoria da transação.
    - **amt**: O valor da transação.
    - **city**: A cidade onde a transação ocorreu.
    - **state**: O estado onde a transação ocorreu.
    - **lat**: A latitude da localização da transação.
    - **long**: A longitude da localização da transação.
    - **city_pop**: A população da cidade onde a transação ocorreu.
    - **merch_lat**: A latitude do comércio associado à transação.
    - **merch_long**: A longitude do comércio associado à transação.

    Retorna um objeto contendo um valor booleano que indica se a transação 
    é considerada fraudulenta.
    """
    if model_loader.model is None:
        raise HTTPException(
            status_code=404, detail="Modelo não carregado e/ou não existente")

    return model_loader.predict_is_fraud(features)
