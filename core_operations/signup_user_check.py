import logging
import hashlib


from database import Database
from utilities.email.send_email import SendEmail


class SignupUser:
    def __init__(self) -> None:
        pass


    def check_exsisting_user_core(self, emailid):
        logging.info("Function -->check_exsisting_user_core")
        db = Database().database_response()
        user_collection = db["user_data"]
        data = user_collection.find_one({"email_id" : emailid},{"_id" : 0})
        if data:
            return "User Exsists"
        else:
            return "Is New User"

    def signup_user_details(self, data):
        db = Database().database_response()
        user_collection = db["user_data"]
        email_id = data["email"]
        user_name = data["user_name"]
        response = SendEmail().send_otp_to_email(email_id, user_name)
        if response == "Failed":
            return "otp not sent"
        else:
            return response
        password = hashlib.md5(password.encode('utf-8')).hexdigest()
        try:
            user_collection.insert_one({"email_id" : email_id, "password" : password, "user_name" : user_name})
            return True
        except Exception as e:
            print("Exception occured")
            print(e)
            return False


    def verify_otp_from_db(self,form_data):
        otp = form_data.get("otp", None)
        request_id = form_data.get("request_id", None)
        db = Database().database_response()
        print("working")
        collection = db["otp_collection"]
        print("Working twice")
        request_data = collection.find_one({"request_id" : request_id},{"_id" : 0})
        if request_data and request_data["otp"]  == otp:
            return "OTP VERIFIED"
        return "OTP FAILED"

        


