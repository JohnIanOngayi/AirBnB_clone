#!/usr/bin/python3

"""
Module That Stores Data For The Whole Project in JSON Format
"""

import json
from models.base_model import BaseModel
from models.city import City
from models.user import User
from models.place import Place
from models.state import State
from models.review import Review
from models.amenity import Amenity


class FileStorage:
    """
    Storage Class For the Project

    Attributes:
    __file_path (str): JSON file to be used
    __objects (dict): will store all object dicts

    TestCases
    > Check types
    > Check contents
    > file.json should be empty on first run
    > Check text format in the storage classes
    > Check for type after instaniation from storage file
    """
    __file_path = "file.json"
    __objects = dict()

    def all(self):
        """
        Returns __objects dict
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serialises __objects in JSON to __file_path
        """
        obj_dict = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w', encoding="utf-8") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """
        Deserialises JSON file to __objects
        """
        try:
            with open(FileStorage.__file_path, encoding="utf-8") as f:
                obj_dict = json.load(f)
                for k, v in obj_dict.items():
                    class_name = eval(v["__class__"])
                    del v['__class__']
                    FileStorage.__objects[k] = class_name(**v)
        except FileNotFoundError:
            pass
