from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import database_exists
from flask_login import LoginManager
from .models import db
from .models import User

'''
This is the main entry point for the Flask application. we configure the app, 
initialize the database, and register blueprints.
'''

#configure the app
def configure_app(app):
    app.config['SECRET_KEY'] = 'secret-key-goes-here'
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{app.root_path}/DB/db.sqlite"

#register blueprints
def register_blueprints(app):
    from .auth.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    from .mainpage.mainpage import main as main_blueprint
    app.register_blueprint(main_blueprint)

#configure the app and initialize the database
def create_app():

    configure_app(app)
    db.init_app(app)
    
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(int(user_id))
    if not database_exists(f"sqlite:///{app.root_path}/DB/db.sqlite"):
        with app.app_context():
            db.create_all()

    register_blueprints(app)

    return app


app = Flask(__name__)
app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
