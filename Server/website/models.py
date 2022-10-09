import email
from enum import unique
from . import DB 
from flask_login import UserMixin





class User(DB.Model,UserMixin):
    id = DB.Column(DB.Integer, primary_key=True)
    email = DB.Column(DB.String(200), unique=True)
    password = DB.Column(DB.String(200), unique=False)
    name = DB.Column(DB.String(200), unique=True)
