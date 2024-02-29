"""User model"""
from api.v1.views import db
from .basemodel import BaseModel


class User(BaseModel, db.Model):
    """ User model db representation"""

    __tablename__ = "users"

    name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    phone = db.Column(db.String(128), nullable=False)
    password = db.Column(db.String(128), nullable=False)

    review = db.relationship('Review', back_populates='user')
