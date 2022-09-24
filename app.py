import email
from flask import Flask, request
from interface.signup_user import SignUp
app = Flask(__name__)

@app.route("/")
def hello_world():
    return {"Doddi" : "Girish"}

#signup route
@app.route("/signup", methods=['POST'])
def signup():
    data = request.form
    emailid = data.get("emailId")
    password = data.get("password")
    user_name = data.get("userName")
    check_for_exsisting_user = SignUp().check_exsisting_user(emailid)
    if not check_for_exsisting_user:
        user_data = {
            "emailId" : emailid,
            "password" : password,
            "user_name" : user_name
        }
        SignUp().add_user(user_data)
        return {"User" : "Signup successfully happend"}
    else:
        return {"User" : "Already present, Couldn't signup"}



@app.route("/check", methods=['POST'])
def check(data):
    return data



if __name__ == "__main__":
    app.run(host = "127.0.0.1", port = 8080, debug=True)