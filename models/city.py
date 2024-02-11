#!/usr/bin/python3
"""
Module for City class, inherits from BaseModel
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    City class inherits from BaseModel
    Attributes:
        state_id (str): empty string
        name (str): empty string
    """
    state_id = ""
    name = ""
