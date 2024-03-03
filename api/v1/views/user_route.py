"""module suppies routes for user resource"""
from models.user import User
from . import db, login_manager

from flask import Blueprint, request, jsonify, session
from flask_login import login_user, logout_user, current_user, login_required

user_bp = Blueprint('user_bp', __name__)


@user_bp.route('/users', methods=['POST'], strict_slashes=False)
def create_user():
    """
    Creates a user
    """
    if not request.json:
        return jsonify({'error': 'Not a JSON'}), 404

    required = ['name', 'email', 'phone', 'password']
    for attribute in required:
        if attribute not in request.json:
            return jsonify({'error': f'Missing {attribute}'}), 400
    
    data = request.json
    existing_user = User.query.filter(User.email == data['email']).first()
    if existing_user:
        return jsonify({'Status': 'User already Exists'}), 400
    user = User(name=data['name'], email=data['email'], phone=data['phone'])
    user.set_password(data['password'])
    db.session.add(user)
    db.session.commit()
    return jsonify(user.todict()), 200


@user_bp.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
def edit_user(user_id):
    """
    edit User record
    """

    # get user record by id
    user = User.query.filter(User.id == user_id).first()
    if user is None:
        return jsonify({'Status': 'User ID doesn\'t exit'}), 404

    required = ['name', 'email', 'phone', 'password']
    for field in required:
        key = request.json.get(field)
        if key:
            setattr(user, field, key)
    db.session.commit()
    return jsonify(user.todict()), 200


@user_bp.route('/users/login', methods=['POST'], strict_slashes=False)
def user_login():
    """
    Authenticate User credentials and login user
    """

    required = ['email', 'password']
    for attribute in required:
        if attribute not in request.json:
            return jsonify({'error': f'Missing {attribute}'}), 400

    data = request.json
    user = User.query.filter(User.email == data['email']).first()
    if user and user.check_password(data['password']):
        login_user(user)
        return jsonify({'Status': 'SUCCESS'}), 200
    else:
        return jsonify({'Status': 'Invalid User'}), 400


@user_bp.route('/users/logout', methods=['GET'], strict_slashes=False)
@login_required
def user_logout():
        """
        logout current user
        """

        logout_user()
        return jsonify({'Logout': 'SUCCESS'})

@login_manager.user_loader
def load_user(user_id):
    """
    Check if user is logged-in on every request
    """

    if user_id is not None:
        return User.query.get(user_id)
    return None


@login_manager.unauthorized_handler
def unauthorized():
    """
    Handle authorized access
    """

    return jsonify({'Login': 'Required'}), 400
