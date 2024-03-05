"""Events model"""
from api.v1.views import db
from .basemodel import BaseModel
from datetime import datetime


class Event(BaseModel, db.Model):
    """ Review model db representation"""

    __tablename__ = "events"

    name = db.Column(db.String(128), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    city = db.Column(db.String(128), nullable=False)
    date = db.Column(db.Date, nullable=False)
    time = db.Column(db.Time, nullable=False)
    venue = db.Column(db.String(128), nullable=False)
    host_id = db.Column(
            db.String(128),
            db.ForeignKey('hosts.id'),
            nullable=False
            )

    my_review = db.relationship('Review', back_populates='my_event')

    def __init__(self, name, description, city, date, time, venue, host_id):
        """ Initializes Events object"""
        super().__init__()
        self.name = name
        self.description = description
        self.city = city
        self.date = date
        self.time = time
        self.venue = venue
        self.host_id = host_id
