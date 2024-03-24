#stores database models
from . import db #importing from the current folder the db from . instead of from website
from flask_login import UserMixin #gives userobject things specific for FlaskLogin module
from sqlalchemy.sql import func 

class User(db.Model, UserMixin):
    #define all of the columns we want to have stored inside the database
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note') #every note will be added to the relationship with this user

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(100000)) #each note can only be 10,000 characters long
    date = db.Column(db.DateTime(timezone=True), default=func.now()) #func.now stores the current date and time when the note is created
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) #we have to pass a valid id of an existing user to this field, we are referencing the primary key of the user model
