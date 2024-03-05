""" Host route test case module """
import unittest
from api.v1.app import app
from api.v1.views import db
from models.host import Host


class TestHostView(unittest.TestCase):
    """
    Test host routes
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

    def test_host_creation(self):
        """
        Test creating a new user
        """
        # check if user exist and skip test
        with app.app_context():
            email = 'johnfake@example.com'
            existing_host = Host.query.filter(Host.email == email).first()
            if existing_host:
                return
        data = {
                'name': 'John fake',
                'email': 'johnfake@example.com',
                'password': 'pass',
                'phone': '123'
                }
        response = self.app.post('/api/v1/hosts', json=data)
        self.assertEqual(response.status_code, 201)

    def test_edit_host(self):
        """
        Test editing host info
        """

        data = {'name': 'John fake'}
        url = '/api/v1/hosts/1db1e6e0-faf0-40c2-a6d1-254e01dcdb8a'
        response = self.app.put(url, json=data)
        self.assertEqual(response.status_code, 200)

    def test_get_host_info(self):
        """
        Test getting host info by host id
        """
        url = '/api/v1/hosts/1db1e6e0-faf0-40c2-a6d1-254e01dcdb8a'
        response = self.app.get(url)
        self.assertEqual(response.status_code, 200)

    def test_get_host_list(self):
        """
        Test getting host list
        """

        url = '/api/v1/hosts'
        response = self.app.get(url)
        self.assertEqual(response.status_code, 200)

    def test_host_login(self):
        """
        Testing host login
        """

        data = {
                'email': 'johnfake@example.com',
                'password': 'pass'
                }
        response = self.app.post('/api/v1/hosts/login', json=data)
        self.assertEqual(response.status_code, 200)
