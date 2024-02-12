#!/usr/bin/python3
"""This module tests the console model for edge cases
"""
import cmd
import datetime
import json
import uuid
import os
import re
import unittest
from io import StringIO
import sys
from unittest.mock import patch
sys.path.append("..")
from console import HBNBCommand
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage


class TestConsole(unittest.TestCase):

    """Tests HBNBCommand console."""
    def setUp(self):
        """Sets up test cases."""
        if os.path.isfile("file.json"):
            os.remove("file.json")
        self.resetStorage()

    def resetStorage(self):
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def help_test_do_show(self, classname):
        """Helps test the show command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create {}".format(classname))
        uid = f.getvalue()[:-1]
        self.assertTrue(len(uid) > 0)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show {} {}".format(classname, uid))
        s = f.getvalue()[:-1]
        self.assertTrue(uid in s)


if __name__ == "__main__":
    unittest.main
