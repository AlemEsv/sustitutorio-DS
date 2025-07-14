from interfaces import IRepository
import hashlib
import json


class OrderService:
    def __init__(self, repo: IRepository):
        self.repo = repo

    def process(self, request_data):
        # Procesar datos del usuario
        user_data = request_data.data
        
        # Simular procesamiento de datos
        processed_data = {
            "usuario": user_data.usuario.lower(),
            "contraseña": hashlib.sha256(user_data.contraseña.encode()).hexdigest(),
            "timestamp": self.repo.get_timestamp()
        }
        
        # Guardar en el repositorio
        self.repo.save(request_data.id, processed_data)
        
        # Retornar respuesta procesada
        return {
            "id": request_data.id,
            "data_procesada": processed_data
        }
