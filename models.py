from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
'''
The user model represents what it means for the app to have a user. 
This tutorial will require fields for an email address, password, and name. 
In future applications, you may decide you want much more information to be stored per user. You can add things like birthdays, profile pictures, locations, or any user preferences.
'''
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))