from interfaces import IUserRepository


class UserService:
    def __init__(self, repo: IUserRepository):
        self.repo = repo

    def welcome_user(self, user_id: str):
        user = self.repo.get_user(user_id)
        return f"Hola {user['name']}"
