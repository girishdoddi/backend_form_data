from imp import reload
import json
from site import check_enableusersite
from tabnanny import check
from flask import Flask, request
from interface.signup_user import SignUp
app = Flask(__name__)
from werkzeug.datastructures import ImmutableMultiDict
@app.route("/")
def hello_world():
    return {"Doddi" : "Girish"}

#signup route
@app.route("/signup", methods=['POST'])
def signup():
    data = ImmutableMultiDict(request.form)
    data.to_dict(flat=False)
    check_for_exsisting_user = SignUp().verify_user(data)
    print(check_for_exsisting_user)
    if check_for_exsisting_user == "Exsisting User":
        return {"User" :"Already exsist"}
    else:
        return {"request_id" : check_for_exsisting_user}


@app.route("/verify/otp", methods = ["POST"])
def verify_otp():
    data = request.data
    data = json.loads(data)
    print(data)
    resp = SignUp().verify_otp(data)
    return resp



if __name__ == "__main__":
    app.run(host = "127.0.0.1", port = 8080, debug=True)