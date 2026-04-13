from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

login_manager = LoginManager()

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'dev-secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tempusmemoria.db'
    db.init_app(app)
    with app.app_context():
        from app import models
        db.create_all()
    from app.routes import main
    app.register_blueprint(main)
    login_manager.login_view = 'main.login'
    login_manager.init_app(app)


    return app