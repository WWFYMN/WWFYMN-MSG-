import imp
from operator import imod
from urllib.parse import urlparse
from flask import Flask

SECRET_KEY='asdoijasdiojsajiodasj'

def create_app():
    app=Flask(__name__)
    app.config['SECRET_KEY']=SECRET_KEY
    from .views import views
    from .auth import auth
    app.register_blueprint(views, url_prefix='/' )
    app.register_blueprint(auth, url_prefix='/')
    return app