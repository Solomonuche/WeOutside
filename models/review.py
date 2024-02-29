"""Review model"""
from api.v1.views import db
from .basemodel import BaseModel


class Review(BaseModel, db.Model):
    """ Review model db representation"""

    __tablename__ = "reviews"

    description = db.Column(db.String(500), nullable=False)
    user_id = db.Column(db.String(126), db.ForeignKey('users.id'), nullable=False)
    #event_id = db.Column(db.String, db.ForeignKey('events.id'), nullable=False)

    # Relationships
    user = db.relationship('User', back_populates='review')
    #event = db.relationship('Event', back_populates='review')
