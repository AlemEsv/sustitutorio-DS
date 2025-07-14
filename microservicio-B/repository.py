from interfaces import IRepository


class InventoryRepository(IRepository):
    def __init__(self):
        # Simulación de base de datos en memoria
        self.inventory_db = {}
        self.user_items_db = {
            "1": ["item_001", "item_002", "item_003"],
            "2": ["item_004", "item_005"],
            "3": ["item_006", "item_007", "item_008", "item_009"],
        }
        self.user_permissions_db = {
            "admin": ["read", "write", "delete"],
            "user": ["read"],
            "manager": ["read", "write"],
        }

    def get_user_items(self, user_id: str):
        return self.user_items_db.get(user_id, [])

    def get_user_permissions(self, username: str):
        # Asignar permisos basados en el nombre de usuario
        if "admin" in username.lower():
            return self.user_permissions_db["admin"]
        elif "manager" in username.lower():
            return self.user_permissions_db["manager"]
        else:
            return self.user_permissions_db["user"]

    def save_inventory_access(self, user_id: str, inventory_data: dict):
        self.inventory_db[user_id] = inventory_data
        return True

    def get_inventory_access(self, user_id: str):
        return self.inventory_db.get(user_id, None)
