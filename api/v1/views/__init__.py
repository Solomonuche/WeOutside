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
            'mysql+mysqldb://root:password@localhost/weoutside_db')
    app.config['SQLALCHEMY_ECHO'] = False
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        # register blueprint
        from .user_route import user_bp
        from .event_route import event_bp
        app.register_blueprint(user_bp, url_prefix='/api/v1')
        app.register_blueprint(event_bp, url_prefix='/api/v1')
        db.create_all()

    return app
