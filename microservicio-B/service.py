from interfaces import IRepository
import datetime


class InventoryService:
    def __init__(self, repo: IRepository):
        self.repo = repo

    def process(self, request_data):
        # Recibir datos procesados del microservicio A
        user_id = request_data.id
        processed_data = request_data.data_procesada
        
        # Transformar datos para inventario basado en el usuario
        inventory_data = {
            "user_id": user_id,
            "usuario": processed_data.usuario,
            "items_asignados": self.repo.get_user_items(user_id),
            "permisos_inventario": self.repo.get_user_permissions(processed_data.usuario),
            "timestamp_acceso": processed_data.timestamp,
            "timestamp_inventario": datetime.datetime.now().isoformat()
        }
        
        # Guardar en el repositorio
        self.repo.save_inventory_access(user_id, inventory_data)
        
        # Retornar inventario transformado
        return {
            "status": "success",
            "inventory_data": inventory_data,
            "message": f"Inventario procesado para usuario {processed_data.usuario}"
        }
