"""Review model"""
from api.v1.views import db
from .basemodel import BaseModel
from .event import Event


class Review(BaseModel, db.Model):
    """ Review model db representation"""

    __tablename__ = "reviews"

    description = db.Column(db.String(500), nullable=False)
    user_id = db.Column(db.String(126), db.ForeignKey('users.id'), nullable=False)
    event_id = db.Column(db.String(126), db.ForeignKey('events.id'), nullable=False)

    # Relationships
    my_user = db.relationship('User', back_populates='my_review')
    my_event = db.relationship('Event', back_populates='my_review')
