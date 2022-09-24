import logging
from core_operations.signup_user_check import SignupUser
from database import Database
class SignUp:
    def __init__(self) -> None:
        pass

    def check_exsisting_user(self,emailid):
        logging.info("Function -->check_exsisting_user")
        exsisting_user = SignupUser().check_exsisting_user_core(emailid)
        return exsisting_user

    def add_user(self,user_details):
        logging.info("Function -->add_user")
        db = Database().database_response()
        user_collection = db["user_data"]
        user_collection.insert_one(user_details)