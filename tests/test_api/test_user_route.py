""" User route test case module """
import unittest
from api.v1.app import app
from api.v1.views import db
from models.user import User


class TestUserView(unittest.TestCase):
    """
    Test user routes
    """

    def setUp(self):
        """
        set app test client before every test
        """

        self.app = app.test_client()

    def tearDown(self):
        """
        Clean up after each test if necessary
        """
        with app.app_context():
            db.session.rollback()

    def test_user_creation(self):
        """
        Test creating a new user
        """
        # check if user exist and skip test
        with app.app_context():
            email = 'johnfake@example.com'
            existing_user = User.query.filter(User.email == email).first()
            if existing_user:
                return
        data = {
                'name': 'John fake',
                'email': 'johnfake@example.com',
                'password': 'pass',
                'phone': '123'
                }
        response = self.app.post('/api/v1/users', json=data)
        self.assertEqual(response.status_code, 201)

    def test_edit_user(self):
        """
        Test editing user info
        """

        data = {'name': 'John fake'}
        url = '/api/v1/users/a0244655-e89c-48a4-819b-032c1bde86a1'
        response = self.app.put(url, json=data)
        self.assertEqual(response.status_code, 200)

    def test_user_login(self):
        """
        Testing user login
        """

        data = {
                'email': 'johnfake@example.com',
                'password': 'pass'
                }
        response = self.app.post('/api/v1/users/login', json=data)
        self.assertEqual(response.status_code, 200)
