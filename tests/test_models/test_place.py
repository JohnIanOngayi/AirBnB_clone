#!/usr/bin/python3

"""
Module Contains Test Cases for class Place
"""
import unittest
import os
from models.place import Place
from models.engine.file_storage import FileStorage
from models import storage


class TestPlace(unittest.TestCase):
    """
    Class contains test cases for class Place
    """

    def setUp(self) -> None:
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_init(self):
        A = Place()
        self.assertEqual(A.city_id, "")
        self.assertEqual(A.user_id, "")
        self.assertEqual(A.name, "")
        self.assertEqual(A.description, "")
        self.assertEqual(A.number_rooms, 0)
        self.assertEqual(A.number_bathrooms, 0)
        self.assertEqual(A.max_guest, 0)
        self.assertEqual(A.price_by_night, 0)
        self.assertEqual(A.latitude, 0.0)
        self.assertEqual(A.longitude, 0.0)
        self.assertEqual(A.amenity_ids, [])

        if __name__ == "__main__":
            unittest.main()
