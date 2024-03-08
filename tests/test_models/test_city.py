#!/usr/bin/python3

"""
Module contains test cases for class City
"""
from models.city import City
from models.engine.file_storage import FileStorage
import models
import unittest
import os


class TestCity(unittest.TestCase):
    """
    unittest class to test class City
    """

    def setup(self):
        """
        Set up method
        """
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_no_args(self):
        """
        Tests instaniation of object with no arguments passed
        """
        A = City()
        self.assertEqual(A.name, "")
        self.assertGreater(A.id, "")
