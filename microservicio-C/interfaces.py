from abc import ABC, abstractmethod


class IUserRepository(ABC):
    @abstractmethod
    def get_user(self, user_id: str):
        pass
