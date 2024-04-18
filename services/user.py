from services.base import BaseRepository
from models.user import UserModel


class UserRepository(BaseRepository):
    model = UserModel
