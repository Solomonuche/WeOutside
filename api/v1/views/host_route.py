"""module suppies routes for user resource"""
from models.host import Host
from . import db, login_manager

from flask import Blueprint, request, jsonify
from flask_login import login_user, logout_user, current_user, login_required

host_bp = Blueprint('host_bp', __name__)


@host_bp.route('/hosts', methods=['POST'], strict_slashes=False)
def create_host():
    """
    Creates a host account
    """
    required = ['name', 'email', 'phone', 'password']
    for attribute in required:
        if attribute not in request.json:
            return jsonify({'error': f'Missing {attribute}'}), 400
    
    data = request.json
    existing_host = Host.query.filter(Host.email == data['email']).first()
    if existing_host:
        return jsonify({'Status': 'Host already Exists'}), 400
    host = Host(name=data['name'], email=data['email'], phone=data['phone'])
    host.set_password(data['password'])
    db.session.add(host)
    db.session.commit()
    return jsonify(host.todict()), 200


@host_bp.route('/hosts/<host_id>', methods=['PUT'], strict_slashes=False)
def edit_host(host_id):
    """
    edit Host record
    """

    # get user record by id
    host = Host.query.filter(Host.id == host_id).first()
    if host is None:
        return jsonify({'Status': 'Host ID doesn\'t exit'}), 404

    required = ['name', 'email', 'phone', 'password']
    for field in required:
        key = request.json.get(field)
        if key:
            setattr(host, field, key)
    db.session.commit()
    return jsonify(host.todict()), 200


@host_bp.route('/hosts', methods=['GET'], strict_slashes=False)
def host_list():
    """
    Returns a list of all hosts in the database
    """

    hosts = Host.query.all()
    all_host = []
    for host in hosts:
        all_host.append(host.todict())

    return jsonify(all_host), 200


@host_bp.route('/hosts/<host_id>', methods=['GET'], strict_slashes=False)
def host_info(host_id):
    """"
    Returns a host info using host id
    """

    host = Host.query.filter(Host.id == host_id).first()
    if host is None:
        return jsonify({'Status': 'Host ID doesn\'t exit'}), 404
    return jsonify(host.todict()), 200


@host_bp.route('/hosts/login', methods=['POST'], strict_slashes=False)
def host_login():
    """
    Authenticate Host credentials and login Host
    """

    required = ['email', 'password']
    for attribute in required:
        if attribute not in request.json:
            return jsonify({'error': f'Missing {attribute}'}), 400

    data = request.json
    host = Host.query.filter(Host.email == data['email']).first()
    if host and host.check_password(data['password']):
        login_user(host)
        return jsonify({'Status': 'SUCCESS'}), 200
    else:
        return jsonify({'Status': 'Invalid User'}), 400


@host_bp.route('/hosts/logout', methods=['GET'], strict_slashes=False)
@login_required
def host_logout():
        """
        logout current host
        """

        logout_user()
        return jsonify({'Logout': 'SUCCESS'})

@login_manager.user_loader
def load_user(user_id):
    """
    Check if host is logged-in on every request
    """

    if user_id is not None:
        return Host.query.get(user_id)
    return None


@login_manager.unauthorized_handler
def unauthorized():
    """
    Handle authorized access
    """

    return jsonify({'Login': 'Required'}), 400
