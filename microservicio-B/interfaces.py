from abc import ABC, abstractmethod


class IRepository(ABC):
    @abstractmethod
    def get_user_items(self, user_id: str):
        pass
    
    @abstractmethod
    def get_user_permissions(self, username: str):
        pass
    
    @abstractmethod
    def save_inventory_access(self, user_id: str, inventory_data: dict):
        pass
    
    @abstractmethod
    def get_inventory_access(self, user_id: str):
        pass
