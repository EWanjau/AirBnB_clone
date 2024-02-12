#!/usr/bin/python3
"""Unittest module for the FileStorage class"""

import re
import json
import os
import unittest
from datetime import datetime
import sys
sys.path.append("..")
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage


class TestFileStorage(unittest.TestCase):
    """tests the file storage module"""

    def resetStorage(self):
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def tearDown(self):
        """Tears down test methods."""
        self.resetStorage()
        pass

    def test_instance(self):
        """Tests object formation of the storage class"""
        self.assertEqual(type(storage).__name__, "FileStorage")

    def test_instance_without_args(self):
        """tests the instantiation without arguments"""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            FileStorage.__init__()
        msg = "descriptor '__init__' of 'object' object needs an argument"
        self.assertEqual(str(e.exception), msg)

    def test_instance_with_more_args(self):
        """Tests instantiation method with many arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            b = FileStorage(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
        msg = "FileStorage() takes no arguments"
        self.assertEqual(str(e.exception), msg)

    def test_save_no_args(self):
        """Tests save() with no arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            FileStorage.save()
        msg = "FileStorage.save() missing 1 required\
            positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

    def test_save_excess_args(self):
        """Tests save() with too many arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            FileStorage.save(self, 98)
        msg = "FileStorage.save() takes 1 positional\
            argument but 2 were given"
        self.assertEqual(str(e.exception), msg)

    def test_reload_no_args(self):
        """Tests reload() with no arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            FileStorage.reload()
        msg = "FileStorage.reload() missing 1 required\
            positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

    def test_reload_excess_args(self):
        """Tests reload() with too many arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            FileStorage.reload(self, 98)
        msg = "FileStorage.reload() takes 1 positional\
            argument but 2 were given"
        self.assertEqual(str(e.exception), msg)

    if __name__ == "__main__":
        unittest.main()
