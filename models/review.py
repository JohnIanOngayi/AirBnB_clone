#!/usr/bin/python3

"""
Module conatins class Review
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Class defines a Review

    Attributes:
    place_id (str)
    user_id (str)
    text (str)
    """
    place_id = ""
    user_id = ""
    text = ""
