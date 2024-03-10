#!/usr/bin/python3

"""
Module Contains unittest Test Cases For The Console
"""

from ast import Str
import sys
import unittest
import os
from io import StringIO
from unittest.mock import patch
from models.engine.file_storage import FileStorage
from console import HBNBCommand
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.amenity import Amenity
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models import storage


class TestConsole(unittest.TestCase):
    """
    Class defines test cases for AirBnB console
    """

    def setUp(self) -> None:
        """Set up Method for Test Class"""
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def clean_it(self) -> None:
        """Helper method that deletes instances within iterations"""
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_help(self) -> None:
        """Testing help command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help quit")
            captured_out = f.getvalue()
            expected = "Quit command to exit the program\n        \n"
            self.assertEqual(expected, captured_out)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help EOF")
            captured_out = f.getvalue()
            expected = "Quits the Console\n        \n"
            self.assertEqual(expected, captured_out)

    def test_do_create(self) -> None:
        """Testing the create methods"""
        for _ in HBNBCommand.CLS:
            _class = eval(_)
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("create {}".format(_class))
                captured_out = f.getvalue()
                self.assertTrue(len(captured_out[:-1]) > 0)
            _id = captured_out[:-1]

            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("show {} {}".format(_class, _id))
                output = f.getvalue()
                self.assertTrue(_id in output)
                self.clean_it()

        for _ in HBNBCommand.CLS:
            _class = eval(_)
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("{}.create()".format(_class))
                captured_out = f.getvalue()
                self.assertTrue(len(captured_out[:-1]) > 0)
            _id = captured_out[:-1]

            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("{}.show({})".format(_class, _id))
                output = f.getvalue()
                self.assertTrue(_id in output)
                self.clean_it()

    def test_do_create_error(self) -> None:
        """Test them create errors"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            captured_out = f.getvalue()
            expected = "** class name missing **"
            self.assertEqual(captured_out[:-1], expected)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create bundas")
            captured_out = f.getvalue()
            expected = "** class doesn't exist **"
            self.assertEqual(captured_out[:-1], expected)

    def test_do_show_errors(self) -> None:
        """Test show method errors"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show")
            captured_out = f.getvalue()
            expected = "** class name missing **"
            self.assertEqual(captured_out[:-1], expected)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show bundas")
            captured_out = f.getvalue()
            expected = "** class doesn't exist **"
            self.assertEqual(captured_out[:-1], expected)


if __name__ == "__main__":
    unittest.main()
