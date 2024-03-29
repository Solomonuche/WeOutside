"""User model"""
from api.v1.views import db
from .basemodel import BaseModel
from flask_login import UserMixin
from .review import Review
from .host import Host
from werkzeug.security import generate_password_hash, check_password_hash


user_host = db.Table('user_host',
        db.Column('user_id', db.String(128), db.ForeignKey('users.id')),
        db.Column('host_id', db.String(128), db.ForeignKey('hosts.id'))
        )

        
class User(BaseModel, db.Model, UserMixin):
    """ User model db representation"""

    __tablename__ = "users"

    name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    phone = db.Column(db.String(128), nullable=False)
    password = db.Column(db.String(600), nullable=False)
    image = db.Column(db.String(500), nullable=False, default='avatar.jpg')

    my_review = db.relationship('Review', back_populates='my_user')

    following = db.relationship('Host', secondary=user_host, backref='followers')

    def __init__(self, name, email, phone, image=None):
        """ class constructor"""

        if image:
            self.image = image
        self.name = name
        self.email = email
        self.phone = phone
        super().__init__()

    def set_password(self, password):
        """
        sets a hash password
        """
        self.password = generate_password_hash(
                password,
                method='pbkdf2:sha256'
                )

    def check_password(self, password):
        """
        checks if password is valid
        """
        return check_password_hash(self.password, password)
