#!/usr/bin/python3

"""
Module contains class City
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    Defines a city

    Attributes:
    state_id (str)
    name (str)
    """
    state_id = ""
    name = ""

