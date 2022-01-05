# Import from owner
from typing import List
from model.user.user_model_mysql import User
from database.db_MySQL import SessionLocal


# Call db
db = SessionLocal()


class User_DAO():
    # Login Dao
    def login_DAO(user: User) -> User:
        user_selected = User()
        list_user = UserSub_DAO.get_all_user_DAOsub()

        for user_single in list_user:
            if user.username == user_single.username:
                if user.password == user_single.password:
                    user_selected = User(
                        id=user_single.id,
                        username=user_single.username,
                        password=user_single.password,
                        image_url=user_single.image_url,
                        type_user=user_single.type_user
                    )
                    break
                else:
                    break

        return user_selected


    # Register Dao
    def register_DAO(user: User) -> bool:
        user_status = False
        checking_user = UserSub_DAO.check_same_username_adding_DAOsub(user.username)

        if checking_user == True:
            user_status = False
        else:
            db.add(user)
            db.commit()
            user_status = True
        
        return user_status


# To make sure main class DAO of user can work, need
# new one class same sub_class to write more conditions
# and main class DAO just have main def()
class UserSub_DAO():
    # Get all user
    def get_all_user_DAOsub() -> List[User]:
        user = db.query(User).all()
        return user


    # Conditions to add new
    def check_same_username_adding_DAOsub(username: str) -> bool:
        user_list = UserSub_DAO.get_all_user_DAOsub()
        for user in user_list:
            if username == user.username:
                return True
            else:
                pass
        return False