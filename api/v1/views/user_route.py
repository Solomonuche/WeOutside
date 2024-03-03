"""module suppies routes for user resource"""
from models.user import User
from . import db

from flask import Blueprint, request, jsonify

user_bp = Blueprint('user_bp', __name__)


@user_bp.route('/user', methods=['POST'], strict_slashes=False)
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
    return user.todict(), 200
