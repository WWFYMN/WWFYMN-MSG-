from nis import cat
from flask import Blueprint,render_template,request,flash

def hasNumbers(inputString):
     return any(char.isdigit() for char in inputString)

auth = Blueprint('auth', __name__)

@auth.route('/login',methods=["GET","POST"])
def login():
    data=request.form
    print(data)
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return '<p>logout<p>'

@auth.route("/sign-up",methods=["GET","POST"])
def sign_up():
    if request.method=='POST':
        email = request.form.get("email")
        name = request.form.get("name")
        password = request.form.get("password")
        confpass = request.form.get("password2")
        #print(password , len(password) < 8 and password.lower==password and hasNumbers(password)==False)
        if len(email)<4:
            flash("Invalid email", category="error")
        elif len(name)<3:
            flash("Invalid name, name<3", category="error")
        elif len(password) < 8:
            flash("Invalid password, Password must be 8 or more characters long",category="error")
        else:
            flash("Success",category="success")

    return render_template("signup.html")