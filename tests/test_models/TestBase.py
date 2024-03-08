#!/usr/bin/python3

import unittest
import sys
import uuid
from datetime import datetime
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Testcases for BaseModel"""
    def test_id_is_unique(self):
        """Test instance attribute id uniqueness"""
        model1 = BaseModel()
        model2 = BaseModel()
        self.assertNotEqual(model1.id, model2.id)

    def test_for_kwargs(self):
        """Test instaniation by dictionary"""
        dict3 = {
            "name": "nobody",
            "gender": "a girl",
            "city": "Pentos",
            "age": 15
        }
        model3 = BaseModel(**dict3)
        self.assertEqual(model3.name, "nobody")
        self.assertEqual(model3.gender, "gender")
        self.assertEqual(model3.city, "Pentos")
        self.assertEqual(model3.age, 15)

    def test_created_at_and_updated_at_are_datetime(self):
        """Test whether module works well with datetime"""
        model = BaseModel()
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_str_method(self):
        """Testing String Method"""
        model = BaseModel()
        expected_str = (f"[{model.__class__.__name__}] "
                        f"({model.id}) "
                        f"{model.__dict__}")

        self.assertEqual(str(model), expected_str)

    def test_save_updates_updated_at(self):
        """Test compatibility with FileStorage Class"""
        model = BaseModel()
        initial_updated_at = model.updated_at
        model.save()
        self.assertGreater(model.updated_at, initial_updated_at)

    def test_to_dict_returns_correct_dictionary(self):
        """Test to_dict method"""
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['__class__'], model.__class__.__name__)
        self.assertEqual(model_dict['id'], model.id)
        self.assertEqual(model_dict['created_at'],
                         model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'],
                         model.updated_at.isoformat())


if __name__ == '__main__':
    unittest.main()
