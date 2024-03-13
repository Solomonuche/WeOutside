""" App initilization"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os
from .login_manager_config import login_manager

db = SQLAlchemy()


def create_app():
    """create flask app"""
    app = Flask(__name__)
    cors = CORS(
            app,
            supports_credentials=True,
            resources={'/*': {'origins': '*'}}
            )
    # app configuration
    app.secret_key = os.urandom(32)
    app.config['SQLALCHEMY_DATABASE_URI'] = (
            'mysql+mysqldb://root:password@localhost/weoutside_db')
    app.config['SQLALCHEMY_ECHO'] = False
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SESSION_COOKIE_HTTPONLY'] = True
    app.config['SESSION_TYPE'] = 'filesystem'
    app.config['UPLOAD_FOLDER'] = 'file_uploads/events_img'
    app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.jpeg']

    db.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        # register blueprint
        from .user_route import user_bp
        from .event_route import event_bp
        from .host_route import host_bp
        from .file_upload import upload_bp

        app.register_blueprint(user_bp, url_prefix='/api/v1')
        app.register_blueprint(host_bp, url_prefix='/api/v1')
        app.register_blueprint(event_bp, url_prefix='/api/v1')
        app.register_blueprint(upload_bp, url_prefix='/api/v1')

        db.create_all()

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db.session.remove()

    return app
