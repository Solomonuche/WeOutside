#!/usr/bin/python3
"""Containt tests for review model"""
from tests.base import BaseTestCase
from models.basemodel import BaseModel
from models.event import Event
from models.review import Review
from models.user import User
import unittest

data = {
        "description": "The event was amazing",
        "user_id": "07e34703-5a84-4a77-bd70-46efe52a867f",
        "event_id": "9f0927fc-b2da-4f1b-a9de-4945e8f172c9"
        }


class TestEvent(BaseTestCase):
    """Tests review class"""
    def test_is_subclass(self):
        """Test that review is subclass of BaseModel"""
        review = Review(**data)

        self.assertIsInstance(review, BaseModel)

    def test_obj_attributes(self):
        """Test that review oject has necessary attributes"""
        review = Review(**data)
        self.assertTrue(hasattr(review, "id"))
        self.assertTrue(hasattr(review, "description"))
        self.assertTrue(hasattr(review, "user_id"))
        self.assertTrue(hasattr(review, "event_id"))
        self.assertTrue(hasattr(review, "created_at"))
        self.assertTrue(hasattr(review, "updated_at"))

    def test_different_id(self):
        """Tests each review object is given different ID"""
        review1 = Review(**data)
        review2 = Review(**data)
        self.assertNotEqual(review1.id, review2.id)
