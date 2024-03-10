#!/usr/bin/python3
"""Containt tests for host model"""
from tests.base import BaseTestCase
from models.basemodel import BaseModel
from models.event import Event
from models.review import Review
from models.user import User
from models.host import Host
import unittest

data1 = {
        "name": "John King",
        "password": "passwor__56",
        "email": "king_john@gmail.com",
        "phone": "0723392331"
        }

data2 = {
        "name": "Alex Prince",
        "password": "passwor__56",
        "email": "king_alex@gmail.com",
        "phone": "0723392331"
        }


class TestHost(BaseTestCase):
    """Tests host class"""
    def test_is_subclass(self):
        """Test that host is subclass of BaseModel"""
        host = Host(**data1)

        self.assertIsInstance(host, BaseModel)

    def test_obj_attributes(self):
        """Test that host oject has necessary attributes"""
        host = Host(**data1)
        self.assertTrue(hasattr(host, "id"))
        self.assertTrue(hasattr(host, "name"))
        self.assertTrue(hasattr(host, "email"))
        self.assertTrue(hasattr(host, "phone"))
        self.assertTrue(hasattr(host, "created_at"))
        self.assertTrue(hasattr(host, "updated_at"))

    def test_different_id(self):
        """Tests each event object is given different ID"""
        host1 = Host(**data1)
        host2 = Host(**data2)
        self.assertNotEqual(host1.id, host2.id)
