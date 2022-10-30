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
        message= request.form.get("note")
        if len(message)<1:
            flash("Message too short", category="error")
        else:
            new_message = Message(data = message,user=current_user.name)
            DB.session.add(new_message)
            DB.session.commit()
    return render_template("home.html",user=current_user,Messages=Message)
    
@views.route('/user',methods=["POST","GET"])
@login_required
def user():

    return render_template("user.html",user=current_user)

@views.route('/delete-note', methods=["POST"])
def delete_note():
    note = json.loads(request.data)
    noteid= note["noteId"]
    note = Message.query.get(noteid)
    if note:
        if note.user_id == current_user.id:
            DB.session.delete(note)
            DB.session.commit()
    return jsonify({})
