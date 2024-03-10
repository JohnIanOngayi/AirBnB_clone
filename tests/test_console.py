#!/usr/bin/python3

"""
Module Contains unittest Test Cases For The Console
"""

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
    Class Defines Test Cases For AirBnB Console
    """

    def setUp(self) -> None:
        """Set Up Method For Test Class"""
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def clean_it(self) -> None:
        """Helper Method That Deletes Instances Within Iterations"""
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_help(self) -> None:
        """Testing Help Command"""
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
        """Testing The Create Methods"""
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
        """Test Them Create Errors"""
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
        """Test Show Method Errors"""
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

    def test_do_destroy(self) -> None:
        """Test Destroy Method"""
        for _ in HBNBCommand.CLS:
            _class = eval(_)
            with patch('sys.stdout', new=StringIO()) as e:
                HBNBCommand().onecmd("create {}".format(_class))
                captured_out = e.getvalue()
            _id = captured_out[:-1]

            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("show {} {}".format(_class, _id))
                before = f.getvalue()
                self.assertTrue(_id in before)

    def test_do_destroy_error(self) -> None:
        """Test Destroy Method Errors"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy")
            captured_out = f.getvalue()
            expected = "** class name missing **"
            self.assertEqual(captured_out[:-1], expected)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy bundas")
            captured_out = f.getvalue()
            expected = "** class doesn't exist **"
            self.assertEqual(captured_out[:-1], expected)

            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("destroy User 256666")
                captured_out = f.getvalue()
                expected = "** no instance found **"
                self.assertEqual(captured_out[:-1], expected)

    def test_do_update_error(self) -> None:
        """Test Update Method Errors"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update")
            captured_out = f.getvalue()
            expected = "** class name missing **"
            self.assertEqual(captured_out[:-1], expected)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update bundas")
            captured_out = f.getvalue()
            expected = "** class doesn't exist **"
            self.assertEqual(captured_out[:-1], expected)

            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("update User 256666")
                captured_out = f.getvalue()
                expected = "** no instance found **"
                self.assertEqual(captured_out[:-1], expected)


if __name__ == "__main__":
    unittest.main()
