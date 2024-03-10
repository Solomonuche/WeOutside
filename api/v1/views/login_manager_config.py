"""login manager configs"""

from flask_login import LoginManager
from flask import jsonify

login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id):
    from models.user import User
    from models.host import Host
    """
    Check if user is logged-in on every request
    """
    user = User.query.get(user_id)
    if user:
        return user

    host = Host.query.get(user_id)
    if host:
        return host

    return None


@login_manager.unauthorized_handler
def unauthorized():
    """
    Handle authorized access
    """

    return jsonify({'Login': 'Required'}), 401
