#!/usr/bin/python3
"""Containt tests for review model"""
from models.basemodel import BaseModel
import unittest


class TestEvent(unittest.TestCase):
    """Tests basemodel class"""
    def test_class_type(self):
        """Test instance is of class basemodel"""
        bm = BaseModel()

        self.assertIs(type(bm), BaseModel)

    def test_obj_attributes(self):
        """Test that basemodel oject has necessary attributes"""
        bm = BaseModel()
        self.assertTrue(hasattr(bm, "id"))
        self.assertTrue(hasattr(bm, "created_at"))
        self.assertTrue(hasattr(bm, "updated_at"))

    def test_different_id(self):
        """Tests that basemodel object is given different ID"""
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)
