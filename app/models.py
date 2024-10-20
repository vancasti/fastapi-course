from pydantic import BaseModel, Field
from typing import List

class Fuels(BaseModel):
    gas: float = Field(..., alias="gas(euro/MWh)")
    kerosine: float = Field(..., alias="kerosine(euro/MWh)")
    co2: float = Field(..., alias="co2(euro/ton)")
    wind: float = Field(..., alias="wind(%)")


class PowerPlant(BaseModel):
    name: str
    type: str
    efficiency: float
    pmin: int
    pmax: int


class PowerPlantData(BaseModel):
    load: float
    fuels: Fuels
    powerplants: List[PowerPlant]
