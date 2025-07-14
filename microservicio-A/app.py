from fastapi import FastAPI, Depends
from pydantic import BaseModel
from service import OrderService
from repository import OrderRepository

app = FastAPI()


# dato (usuario y contraseña)
class UserData(BaseModel):
    usuario: str

    contraseña: str


# se pedira id y datos de usuario
class RequestData(BaseModel):
    id: str
    data: UserData


def get_order_service():
    repo = OrderRepository()
    return OrderService(repo)


# consultar estado de la aplicacion
@app.get("/ping")
def ping():
    return {"status": "ok"}


# recibe un archivo json con un dato(id, data: {usuario, contraseña})
# devuelve un archivo json con datos procesados(id, data_procesada)
@app.post("/process")
def handle(request: RequestData, service: OrderService = Depends(get_order_service)):
    return service.process(request)
