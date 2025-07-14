from fastapi import FastAPI, Depends
from service import UserService
from repository import UserRepository

app = FastAPI()


def get_user_service():
    repo = UserRepository()
    return UserService(repo)

# recibe informacion del microservicio B y finaliza el proceso
@app.get("/welcome/{user_id}")
def welcome(user_id: str, service: UserService = Depends(get_user_service)):
    return {"message": service.welcome_user(user_id)}
