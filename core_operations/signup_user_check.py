import logging
from database import Database
class SignupUser:
    def __init__(self) -> None:
        pass


    def check_exsisting_user_core(self, emailid):
        logging.info("Function -->check_exsisting_user_core")
        db = Database().database_response()
        user_collection = db["user_data"]
        user_collection.find_one({"emailId" : emailid},{"_id" : 0})
        if user_collection:
            return True
        else:
            return False


