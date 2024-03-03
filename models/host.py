"""host model"""
from api.v1.views import db
from .basemodel import BaseModel
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class Host(BaseModel, db.Model, UserMixin):
    """ Host model db representation"""

    __tablename__ = "hosts"

    name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    phone = db.Column(db.String(128), nullable=False)
    password = db.Column(db.String(600), nullable=False)

    def __init__(self, name, email, phone):
        """ class constructor"""

        self.name = name
        self.email = email
        self.phone = phone
        super().__init__()

    def set_password(self, password):
        """
        sets a hash password
        """

        self.password = generate_password_hash(password, method='pbkdf2:sha256')

    def check_password(self, password):
        """
        checks if password is valid
        """

        return check_password_hash(self.password, password)
