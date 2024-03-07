#!/usr/bin/python3
"""module contains setup and teardown of test app"""
from flask_testing import TestCase
from api.v1.views import create_app, db
from config_test import TestConfig


class BaseTestCase(TestCase):
    """
    Initializes the flask application with test configuration
    """
    def create_app(self):
        """creates the app"""
        app = create_app()
        app.config.from_object(TestConfig)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.rollback()
        db.session.remove()
