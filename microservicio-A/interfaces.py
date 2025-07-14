from abc import ABC, abstractmethod


class IRepository(ABC):
    @abstractmethod
    def get(self, item_id: str):
        pass

    @abstractmethod
    def save(self, item_id: str, data: dict):
        pass

    @abstractmethod
    def get_timestamp(self):
        pass
