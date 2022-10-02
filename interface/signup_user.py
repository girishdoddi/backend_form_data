import logging
from core_operations.signup_user_check import SignupUser
from database import Database
class SignUp:
    def __init__(self) -> None:
        pass

    def verify_user(self,form_data):
        email_id = form_data["email"]
        user = SignupUser().check_exsisting_user_core(email_id)
        if user == "Exsisting User":
            return "Exsisting User"
        else:
            check = SignupUser().signup_user_details(form_data)
            return check

    def add_user(self,user_details):
        logging.info("Function -->add_user")
        db = Database().database_response()
        user_collection = db["user_data"]
        user_collection.insert_one(user_details)
    

    def verify_otp(self, request_body):
        logging.info("Function-->verify_otp")
        print("Working")
        verified = SignupUser().verify_otp_from_db(request_body)
        return verified

