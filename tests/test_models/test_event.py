#!/usr/bin/python3
"""Containt tests for event model"""
from tests.base import BaseTestCase
from models.basemodel import BaseModel
from models.event import Event
from models.review import Review
from models.user import User
import unittest

data = {
        "city": "Nairobi",
        "date": "2024-03-12",
        "description": "lets code!!",
        "host_id": "892f25e2-18ca-49aa-8b6f-9ec85d8015cb",
        "name": "Lets Code",
        "time": "00:09:00",
        "venue": "Nairobi Garage"
        }


class TestEvent(BaseTestCase):
    """Tests event class"""
    def test_is_subclass(self):
        """Test that event is subclass of BaseModel"""
        event = Event(**data)

        self.assertIsInstance(event, BaseModel)

    def test_obj_attributes(self):
        """Test that event oject has necessary attributes"""
        event = Event(**data)
        self.assertTrue(hasattr(event, "id"))
        self.assertTrue(hasattr(event, "name"))
        self.assertTrue(hasattr(event, "city"))
        self.assertTrue(hasattr(event, "date"))
        self.assertTrue(hasattr(event, "created_at"))
        self.assertTrue(hasattr(event, "updated_at"))
        self.assertTrue(hasattr(event, "time"))
        self.assertTrue(hasattr(event, "venue"))
        self.assertTrue(hasattr(event, "host_id"))
        self.assertTrue(hasattr(event, "description"))

    def test_different_id(self):
        """Tests each event object is given different ID"""
        event1 = Event(**data)
        event2 = Event(**data)
        self.assertNotEqual(event1.id, event2.id)
