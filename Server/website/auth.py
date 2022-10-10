import email
from nis import cat
from operator import imod
import re
from flask import Blueprint,render_template,request,flash,redirect,url_for
from . import DB
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user

def hasNumbers(inputString):
     return any(char.isdigit() for char in inputString)

auth = Blueprint('auth', __name__)

@auth.route('/login',methods=["GET","POST"])
def login():
    if request.method=="POST":
        email = request.form.get("email")
        password = request.form.get("password")
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash("Logged in", category="success")
                login_user(user,remember=True)
                return redirect(url_for("views.home"))
            else:
                flash("Incorrect password or email", category="error")
    
    return render_template("login.html", user=current_user)
    

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route("/sign-up",methods=["GET","POST"])
def sign_up():
    
    if request.method=='POST':
        email = request.form.get("email")
        name = request.form.get("name")
        password = request.form.get("password")
        confpass = request.form.get("password2")
        user = User.query.filter_by(email=email).first()
        #print(password , len(password) < 8 and password.lower==password and hasNumbers(password)==False)
        if user:
            flash("User already exists",category="error")
        
        elif len(email)<4:
            flash("Invalid email", category="error")
        elif len(name)<3:
            flash("Invalid name, name<3", category="error")
        elif len(password) < 8:
            flash("Invalid password, Password must be 8 or more characters long",category="error")
        else:
            if password==confpass:
                new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha512'))
                DB.session.add(new_user)
                DB.session.commit()
                flash("Success",category="success")
                user = User.query.filter_by(email=email).first()
                login_user(user,remember=True)
                return redirect(url_for("views.home"))
            else:
                flash("Passwords Dont match", category="error")

    return render_template("signup.html", user = current_user)