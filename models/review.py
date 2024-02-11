#!/usr/bin/python3
"""
Module for Review class, inherits from BaseModel
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class inherits from BaseModel
    Attributes:
        place_id (str): empty string
        user_id (str): empty string
        text (str): empty string
    """
    place_id = ""
    user_id = ""
    text = ""
