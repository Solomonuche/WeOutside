"""module suppies routes for event resource"""
from models.event import Event
from models.host import Host
from . import db, login_manager
from datetime import datetime
from flask_login import current_user, login_required

from flask import Blueprint, request, jsonify

event_bp = Blueprint('event_bp', __name__)


@event_bp.route('/events', methods=['GET'], strict_slashes=False)
def return_events():
    """
    Returns a dictionary of lists of events in the database
    """
    events = Event.query.all()
    events_data = [event.todict() for event in events]
    return jsonify(events_data), 200


@event_bp.route('/events/<event_id>', methods=['GET'], strict_slashes=False)
def return_event(event_id):
    """
    Return a dictionary of an event details based on the event id
    """
    event = Event.query.filter(Event.id == event_id).first()
    if event:
        return jsonify(event.todict()), 200
    else:
        return jsonify({'error': 'Event not found'}), 404


@event_bp.route(
        '/hosts/<host_id>/events',
        methods=['POST'],
        strict_slashes=False
        )
@login_required
def create_event(host_id):
    """
    creates an event
    """
    user_type = current_user.__class__.__name__
    if user_type != "Host":
        return jsonify({'error': 'unauthorized'}), 400
    host = Host.query.filter(Host.id == host_id).first()
    if not host:
        return jsonify({'error': 'Host not found'}), 404
    data = request.json
    if not data:
        return jsonify({'error': 'Not a JSON'})
    required = ['name', 'city', 'date', 'time', 'venue']
    for attribute in required:
        if attribute not in data:
            return jsonify({'error': f'Missing {attribute}'}), 400
    data['host_id'] = host_id
    event = Event(**data)
    db.session.add(event)
    db.session.commit()
    return event.todict(), 201


@event_bp.route('/events/<event_id>', methods=['PUT'], strict_slashes=False)
@login_required
def update_event(event_id):
    """
    Updates an event
    """
    event = Event.query.filter(Event.id == event_id).first()
    if not event:
        return jsonify({'error': 'Event not found'}), 404
    data = request.json
    if not data:
        return jsonify({'error': 'Not a JSON'}), 400
    for key, value in data.items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(event, key, value)
    setattr(event, 'updated_at', datetime.utcnow())
    db.session.commit()
    return event.todict(), 200


@event_bp.route('events/<event_id>', methods=['DELETE'], strict_slashes=False)
@login_required
def delete_event(event_id):
    """
    deletes an event
    """
    event = Event.query.filter(Event.id == event_id).first()
    if not event:
        return jsonify({'error': 'Event not found'}), 404
    db.session.delete(event)
    db.session.commit()
    return jsonify({}), 200
