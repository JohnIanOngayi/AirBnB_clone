#!/usr/bin/python3

"""
Module defines class User
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    Subclass of BaseModel that defines a User

    Attributes:
    email string (str)
    password (str)
    first_name (str)
    last_name (str)
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
