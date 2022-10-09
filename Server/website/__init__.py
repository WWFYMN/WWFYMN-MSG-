import imp
from operator import imod
from urllib.parse import urlparse
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

SECRET_KEY='asdoijasdiojsajiodasj'
DB=SQLAlchemy()
DB_NAME = "database.bd"

def create_app():
    app=Flask(__name__)
    app.config['SECRET_KEY']=SECRET_KEY
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    DB.init_app(app)

    from .views import views
    from .auth import auth
    app.register_blueprint(views, url_prefix='/' )
    app.register_blueprint(auth, url_prefix='/')
    return app