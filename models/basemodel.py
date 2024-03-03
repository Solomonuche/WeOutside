""" base model"""
from api.v1.views import db
from datetime import datetime
from uuid import uuid4


class BaseModel():
    """ Base model class representation defining common attribute """

    id = db.Column(db.String(60), primary_key=True, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self):
        """ class constructor"""
        self.id = str(uuid4())

    def todict(self):
        """ return dictionary representation of the obj"""

        obj_dict = {c.name: str(getattr(self, c.name))
                    for c in self.__table__.columns}

        # Remove password field from response body
        if 'password' in obj_dict:
            del obj_dict['password']
        return obj_dict
