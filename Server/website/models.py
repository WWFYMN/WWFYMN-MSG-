import email
from email.policy import default
from enum import unique
from time import timezone
from . import DB 
from flask_login import UserMixin
from sqlalchemy.sql import func


class Message(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    data = DB.Column(DB.String(1000))
    date = DB.Column(DB.DateTime(timezone=True), default=func.now())
    user = DB.Column(DB.String(80))
    #user_id = DB.Column(DB.Integer, DB.ForeignKey("user.id"))
    
class User(DB.Model,UserMixin):
    id = DB.Column(DB.Integer, primary_key=True)
    email = DB.Column(DB.String(200), unique=True)
    password = DB.Column(DB.String(200), unique=False)
    name = DB.Column(DB.String(200), unique=True)
    #messages = DB.relationship("Message")
