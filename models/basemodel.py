""" base model"""
from api.v1.views import db
from datetime import datetime
from uuid import uuid4


class BaseModel():
    """ Base model class representation defining common attribute """

    id = db.Column(db.String(60), primary_key=True, nullable=False, default=uuid4())
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
