#!/usr/bin/python3
"""This module tests the amenity model for edge cases
"""
import time
import json
import uuid
import os
import re
import unittest
from datetime import datetime as datetime
import sys
sys.path.append("..")
from models.amenity import Amenity
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage


class TestAmenity(unittest.TestCase):
    """The module tests the module in edge cases"""

    def setUp(self):
        """Sets up test methods."""
        pass

    def tearDown(self):
        """Tears down test methods."""
        self.resetStorage()
        pass

    def resetStorage(self):
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_Amenity(self):
        """Tests instantiation of Amenity class."""

        a = Amenity()
        self.assertEqual(str(type(a)), "<class 'models.amenity.Amenity'>")
        self.assertIsInstance(a, Amenity)
        self.assertTrue(issubclass(type(a), BaseModel))


if __name__ == "__main__":
    unittest.main()
