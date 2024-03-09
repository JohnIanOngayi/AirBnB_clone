#!/usr/bin/python3

"""
Module Contains The Parent Class BaseModel
"""

import uuid
import datetime
import models


class BaseModel:
    """
    Superclass for the whole project

    Attributes:
    id (str): unique id for instance
    created_at (str): datetime object for instaniation time
    updated_at (str): datetime object for updating time
    """

    def __init__(self, *args, **kwargs):
        """
        Instantiates object of type BaseModel

        Parameters:
        args (tuple): contains attributes of instance
        kwargs (dict): key, value pair for attributes of instance

        TestCases:
        > Pass right and wrong types of args and kwargs
        > Pass invalid values in args and kwargs
        > Check attr types
        > id uniqueness betw two objects
        > created_at uniqueness
        > updated_at > created_at
        """
        tformat = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs is not None and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.datetime.strptime(v, tformat)
                else:
                    self.__dict__[k] = v
            if "id" not in kwargs.keys():
                self.id = f"{uuid.uuid4()}"
        else:
            self.id = f"{uuid.uuid4()}"
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Returns informal str representation of an object
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates updated_at for an instance
        """
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns dictionary for an instance
        """
        my_dict = dict(self.__dict__)
        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["id"] = self.id
        my_dict["updated_at"] = self.updated_at.isoformat()

        return my_dict
