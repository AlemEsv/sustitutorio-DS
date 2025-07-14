from fastapi import FastAPI, Depends
from pydantic import BaseModel
from service import InventoryService
from repository import InventoryRepository

app = FastAPI()


# recibir datos procesados del microservicio A
class ProcessedData(BaseModel):
    usuario: str
    contraseña: str
    timestamp: str


class DataFromMicroserviceA(BaseModel):
    id: str
    data_procesada: ProcessedData


def get_inventory_service():
    repo = InventoryRepository()
    return InventoryService(repo)


@app.get("/ping")
def ping():
    return {"status": "ok"}


# Recibe datos del microservicio A y los transforma para inventario
@app.post("/inventory/process")
def handle(request: DataFromMicroserviceA, service: InventoryService = Depends(get_inventory_service)):
    return service.process(request)


# Endpoint adicional para consultar inventario de un usuario
@app.get("/inventory/user/{user_id}")
def get_user_inventory(user_id: str, service: InventoryService = Depends(get_inventory_service)):
    return service.get_user_inventory(user_id)
