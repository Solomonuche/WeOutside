"""host model"""
from api.v1.views import db
from .basemodel import BaseModel


class Host(BaseModel, db.Model):
    """ Host model db representation"""

    __tablename__ = "hosts"

    name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    phone = db.Column(db.String(128), nullable=False)
    password = db.Column(db.String(128), nullable=False)