#makes the website folder a python package
#allows anything in init.py to be imported into main from website folder 

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy() #initialize a database
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__) #initializes flask, represents name fo the file that was ran
    app.config['SECRET_KEY'] = 'key' #incrypts cookies/session data from website
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}' #SQL alchemy database is located at this location
    db.init_app(app) #takes the database and tells it what app we are using with it, in this case the flask app

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note 

    with app.app_context():
        db.create_all()

    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')


