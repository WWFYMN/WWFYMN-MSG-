from xml.dom.expatbuilder import theDOMImplementation
from .models import Message
from flask import Blueprint, render_template,request,flash,jsonify
from flask_login import  login_required, current_user
from . import DB
from .models import *

import json
from threading import *
views = Blueprint('views', __name__)



@views.route('/',methods=["POST","GET"])
@login_required
def home():
    if request.method=="POST":
        message= request.form.get("msg")
        if len(message)<1:
            flash("Message too short", category="error")
        else:
            new_message = Message(data = message,user=current_user.name)
            DB.session.add(new_message)
            DB.session.commit()

            
    rows = int(str(DB.session.query(Message).count()))
    return render_template("home.html",user=current_user,Messages=Message, rows=rows+12)
    
@views.route('/user',methods=["POST","GET"])
@login_required
def user():

    return render_template("user.html",user=current_user)

@views.route('/Update',methods=["POST","GET"])
@login_required
def Update():
    rows = int(str(DB.session.query(Message).count()))
    return render_template("messages.html",user=current_user,Messages=Message, rows=rows+12)

