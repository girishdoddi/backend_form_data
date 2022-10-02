import smtplib
import random
from uuid import uuid4
import uuid
from database import Database
class SendEmail:
    def __init__(self) -> None:
        pass


    def generate_random_otp(self):
        otp = ""
        for i in range(4):
            otp += str(random.randint(0,9))
        return otp


    def send_otp_to_email(self,email_id, user_name):
        sender_email = "girishdoddi055@gmail.com"
        rec_email = email_id
        password = "pojtrzbidcbzgxwf"
        otp = self.generate_random_otp()
        message = f"Hey {user_name} here is you otp for email verification --> {otp}, Kudos!"
        server = smtplib.SMTP('smtp.gmail.com', 587)
        request_id = uuid4()
        request_id = str(request_id)
        # save request id and otp in database
        db = Database().database_response()
        collection = db["otp_collection"]
        try:
            collection.insert_one({"request_id" : request_id, "otp" : otp})
        except Exception as e:
            print(e)
            print("Failed to insert otp and request id in database")
            return "Failed"
        server.starttls()
        server.login(sender_email, password=password)
        print("Login success")

        #send otp via mail to verify
        server.sendmail(sender_email, rec_email, message)
        print("Email Sent successfuly")
        return request_id