#!/usr/bin/python3
"""This module tests the base model for edge cases
"""


import sys
sys.path.append("..")
import unittest
from datetime import datetime as datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import json
import uuid
import os
import re


class TestBaseModel(unittest.TestCase):
    """test cases for the base model class
    """
    def setup(self):
        """prepare the test methods"""
        pass

    def deleteSetup(self):
        """deletes test methods"""
        self.resetStorage()
        pass

    def resetStorage(self):
        """resets file storage data for the test methods"""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_base_init(self):
        """
        Testing a class BaseModel
        """
        one = BaseModel()
        self.assertIsInstance(one, BaseModel)
        self.assertTrue(issubclass(type(one), BaseModel))
        self.assertIs(type(one), BaseModel)
        one.name = "Monday"
        one.my_number = 89
        self.assertEqual(one.name, "Monday")
        self.assertEqual(one.my_number, 89)

    def test_base_init_without_parameters(self):
        """Tests __init__ with no parameters"""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            BaseModel.__init__()
        msg = "BaseModel.__init__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

    def test_str(self):
        """Test the string printing format method"""
        two = BaseModel()
        rex = re.compile(r"^\[(.*)\] \((.*)\) (.*)$")
        res = rex.match(str(two))
        self.assertIsNotNone(res)
        self.assertEqual(res.group(1), "BaseModel")
        self.assertEqual(res.group(2), two.id)

    def test_save(self):
        """Tests the saving method without any parameters passed"""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            BaseModel.save()
        msg = "BaseModel.save() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

    def test_save_parameters(self):
        """Tests the saving method with more parameters/args passed"""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            BaseModel.save(self, "Parameter")
        msg = "BaseModel.save() takes 1 positional argument but 2 were given"
        self.assertEqual(str(e.exception), msg)

    def test_to_dict(self):
        """Tests the conversion method for dictionaries"""
        a = BaseModel()
        a.name = "ALX"
        a.age = 4
        b = a.to_dict()
        self.assertEqual(b["id"], a.id)
        self.assertEqual(b["created_at"], a.created_at.isoformat())
        self.assertEqual(b["updated_at"], a.updated_at.isoformat())
        self.assertEqual(b["name"], a.name)
        self.assertEqual(b["age"], a.age)

    def test_to_dict_without_parameters(self):
        """Tests to_dict() with no parameters passed."""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            BaseModel.to_dict()
        msg = "BaseModel.to_dict() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

    def test_3_to_dict_more_parameters(self):
        """Tests to_dict() with more parameters."""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            BaseModel.to_dict(self, "work", "serve", "love")
        msg = "BaseModel.to_dict() takes 1 positional argument but 4 were given"
        self.assertEqual(str(e.exception), msg)

    def test_instantiation_process(self):
        """Tests instantiation with **kwargs."""
        b = BaseModel()
        b.name = "ALX"
        b.my_number = 4
        b_json = b.to_dict()
        b_new = BaseModel(**b_json)
        self.assertEqual(b_new.to_dict(), b.to_dict())

if __name__ == '__main__':
    unittest.main()
