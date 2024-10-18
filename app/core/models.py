from pydantic import BaseModel, Field


class RequestModel(BaseModel):
    category: str = Field(..., example="grocery_net")
    amt: float = Field(..., example=12.6)
    city: str = Field(..., example="Mendon")
    state: str = Field(..., example="UT")
    lat: float = Field(..., example=41.71)
    long: float = Field(..., example=-111.9817)
    city_pop: int = Field(..., example=2078)
    merch_lat: float = Field(..., example=42.319998)
    merch_long: float = Field(..., example=-111.552248)


class ResponseModel(BaseModel):
    is_fraud: bool = Field(..., example=True)
    probability: float = Field(..., example=0.90)
