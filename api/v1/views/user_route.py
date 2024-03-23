"""module suppies routes for user resource"""
from models.user import User
from models.host import Host
from . import db, login_manager
from datetime import datetime

from flask import Blueprint, request, jsonify, session
from flask_login import login_user, logout_user, current_user, login_required

user_bp = Blueprint('user_bp', __name__)


@user_bp.route('/users', methods=['POST'], strict_slashes=False)
def create_user():
    """
    Creates a user
    """
    if not request.json:
        return jsonify({'error': 'Not a JSON'}), 400

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
    return jsonify(user.todict()), 201


@user_bp.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
def edit_user(user_id):
    """
    edit User record
    """

    # get user record by id
    user = User.query.filter(User.id == user_id).first()
    if user is None:
        return jsonify({'Status': 'User ID doesn\'t exit'}), 404

    required = ['name', 'email', 'phone', 'password', 'image']
    for field in required:
        key = request.json.get(field)
        if key:
            setattr(user, field, key)
            user.updated_at = datetime.utcnow()
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
        return jsonify({'user_id': user.id}), 200
    else:
        return jsonify({'Status': 'Wrong E-mail or Password'}), 400


@user_bp.route('/users/logout', methods=['GET'], strict_slashes=False)
@login_required
def user_logout():
    """
    logout current user
    """
    logout_user()
    return jsonify({'Logout': 'SUCCESS'}), 200


@user_bp.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
@login_required
def get_user(user_id):
    """
    Returns a dictionary representation of user
    """
    user = User.query.filter(User.id == user_id).first()
    return jsonify(user.todict()), 200


@user_bp.route('/users/<user_id>/followings', methods=['GET'], strict_slashes=False)
@login_required
def get_following(user_id):
    """
    Returns a list of all hosts followed by user
    """
    user = User.query.filter(User.id == user_id).first()
    
    return [host.id for host in user.following]


@user_bp.route('/users/<user_id>/followings', methods=['POST'], strict_slashes=False)
@login_required
def add_following(user_id):
    """
    Adds a host to a list of user followings
    """
    user = User.query.filter(User.id == user_id).first()
    if user is None:
        return jsonify({'Error': 'User Not Found'}), 404
    if current_user != user:
        return jsonify({'Error': 'Not Authorized'}), 401
    host_id = request.json.get('host_id')
    host = Host.query.filter(Host.id == host_id).first()
    user.following.append(host)
    db.session.commit()
    return [host.id for host in user.following], 200

@user_bp.route('/users/<user_id>/followings', methods=['PUT'], strict_slashes=False)
@login_required
def remove_following(user_id):
    """
    Removes a host from a users followings list
    """
    user = User.query.filter(User.id == user_id).first()
    if user is None:
        return jsonify({'Error': 'User Not Found'}), 400
    if current_user != user:
        return jsonify({'Error':'Not Authorized'}), 401
    host_id = request.json.get('host_id')
    host = Host.query.filter(Host.id == host_id).first()
    user.following.remove(host)
    db.session.commit()
    return jsonify({'Status': 'Success'}), 200

@user_bp.route('/users/<user_id>/notfollowings', methods=['GET'], strict_slashes=False)
@login_required
def get_not_following(user_id):
    """
    Returns a list of host a user is not following
    """
    not_following_list = []
    user = User.query.filter(User.id == user_id).first()
    if user is None:
        return jsonify({'Error': 'User Not Found'}), 400
    if current_user != user:
        return jsonify({'Error':'Not Authorized'}), 401
    hosts = Host.query.all()
    for host in hosts:
        if host not in user.following:
            not_following_list.append(host.todict())
    return not_following_list, 200
