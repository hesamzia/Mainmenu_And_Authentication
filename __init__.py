from flask import Flask
import os 
#import config
from flask_sqlalchemy import SQLAlchemy
from flask import Blueprint


# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()
#database_path = os.path.dirname(os.path.realpath(__file__)) + config.DATABASE_PATH

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return "Login Page"

    
def create_app():
    print('Creating app...')
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'secret-key-goes-here'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    db.init_app(app)

    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .mainpage import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app