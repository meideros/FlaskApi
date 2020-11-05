from .base_repository import BaseRepository
from models.user import User
class UserRepository(BaseRepository):
    def __init__(self):
        self.model = User
        super().__init__(self.model)
        
    def find_user_by_email(self, email):
       return  self.model.where("email", email).first()



user_repository = UserRepository()
    

