#!/usr/bin/python3
""" Config class"""


class TestConfig:
    TESTING = True
    con_str = 'mysql+mysqldb://root:password@localhost/weoutside_db'
    SQLALCHEMY_DATABASE_URI = con_str
    SQLALCHEMY_TRACK_MODIFICATIONS = False
