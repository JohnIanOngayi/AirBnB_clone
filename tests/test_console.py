#!/usr/bin/python3

"""
Module Contains unittest Test Cases For The Console
"""

import sys
import io
import unittest
import os
from models.engine.file_storage import FileStorage


class TestConsole(unittest.TestCase):
    """
    Class defines test cases for AirBnB console
    """

    def setUp(self) -> None:
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)
