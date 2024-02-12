#!/usr/bin/python3
"""This module tests the user model for edge cases
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
from models.user import User
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage


class TestUser(unittest.TestCase):

    """Test Cases for the User class."""

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

    def test_instance(self):
        """Tests instantiation of User class."""

        b = User()
        self.assertEqual(str(type(b)), "<class 'models.user.User'>")
        self.assertIsInstance(b, User)
        self.assertTrue(issubclass(type(b), BaseModel))


if __name__ == "__main__":
    unittest.main()
