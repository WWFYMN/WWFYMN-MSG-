
from cmath import log
from re import A
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

#Change this
SECRET_KEY='asdoijasdiojsajiodasj'
#--------------------
DB=SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app=Flask(__name__)
    app.config['SECRET_KEY']=SECRET_KEY
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    DB.init_app(app)

    
    from .views import views
    from .auth import auth
    from .models import User, Message
    app.register_blueprint(views, url_prefix='/' )
    app.register_blueprint(auth, url_prefix='/')
    

    create_database(app)
    login_manager=LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app
def create_database(app):
    if not path.exists("./"+DB_NAME):
        DB.create_all(app=app)
        print("Created database!")
