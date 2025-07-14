from interfaces import IRepository
from datetime import datetime


class OrderRepository(IRepository):
    def __init__(self):
        self.data_store = {}
    
    def get(self, item_id: str):
        return self.data_store.get(item_id, f"dato-{item_id}")
    
    def save(self, item_id: str, data: dict):
        self.data_store[item_id] = data
        return True
    
    def get_timestamp(self):
        return datetime.now().isoformat()
