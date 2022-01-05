# import from python
from typing import List

# Import from owner
from layer.DAO.user_DAO import User_DAO
from model.user.user_model_mysql import User


class User_BUS():
    def login_BUS(user: User) -> User:
        user_login = User_DAO.login_DAO(user)
        return user_login


    def register_BUS(user: User) -> bool:
        user_status = User_DAO.register_DAO(user)
        return user_status
    
    


