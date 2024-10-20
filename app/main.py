from .models import PowerPlantData
from .services import PowerPlantService
from fastapi import FastAPI

app = FastAPI()


@app.post("/productionplan")
def read_item(data: PowerPlantData):
    sorted_plants = PowerPlantService.get_sorted_plants(data)
    production_plan = PowerPlantService.get_production_plant(data, sorted_plants)
    return production_plan
