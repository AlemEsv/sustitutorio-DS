from interfaces import IUserRepository


class UserRepository(IUserRepository):
    def get_user(self, user_id: str):
        return {"id": user_id, "name": "Luis"}
