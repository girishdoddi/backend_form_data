import json
from flask_cors import CORS
from flask import Flask, request, Response,Request
from interface.signup_user import SignUp
from interface.login_user import LoginUser
app = Flask(__name__)
CORS(app)
from werkzeug.datastructures import ImmutableMultiDict
@app.route("/")
def hello_world():
    # req = Request.access_control_request_headers
    # resp = Response.headers["Access-Control-Allow-Origin"] = "*"
    return {"Doddi" : "Girish"},{"Doddi" : "Working"}

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
    return {"resp" : resp}


@app.route("/login", methods = ["POST"])
def verify_ligin():
    data = request.data
    data = json.loads(data)





if __name__ == "__main__":
    app.run(host = "127.0.0.1", port = 8080, debug=True)