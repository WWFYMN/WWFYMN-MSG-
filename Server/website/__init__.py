#from .models import Message
import imp
from flask import Flask , render_template
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from turbo_flask import Turbo
from time import sleep
import threading

#from website.models import Message
#Change this
SECRET_KEY='asdoijasdiojsajiodasj'
#--------------------
DB=SQLAlchemy()
DB_NAME = "database.db"
turbo=Turbo()

def update_load(app,M):
    print("asd")
    with app.app_context():
        while True:
            sleep(1)
            #print("ASD")
            turbo.push(turbo.replace(render_template('messages.html',Messages=M), target='notes'))


def create_app():
    app=Flask(__name__)
    app.config['SECRET_KEY']=SECRET_KEY
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    DB.init_app(app)
    turbo.init_app(app)
    
    
    from .views import views
    from .auth import auth
    from .models import User, Message
    app.register_blueprint(views, url_prefix='/' )
    app.register_blueprint(auth, url_prefix='/')
    

    #create_database(app)
    with app.app_context():
        DB.create_all()
    @app.before_first_request
    def before_first_request():
        thread = threading.Thread(target=update_load, args=[app,Message])
        thread.start()
    before_first_request()
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
