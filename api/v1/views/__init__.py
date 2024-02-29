""" App initilization"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()


def create_app():
    """create flask app"""
    app = Flask(__name__)
    # app configuration
    app.secret_key = os.urandom(32)
    app.config['SQLALCHEMY_DATABASE_URI'] = (
            'mysql+mysqldb://solomon:pass@localhost/weoutside_db')
    app.config['SQLALCHEMY_ECHO'] = False
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        # register blueprint
        
        db.create_all()

    return app
