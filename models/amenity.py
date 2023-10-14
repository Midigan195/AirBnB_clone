#!/usr/bin/python3
"""This is the amenity class"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represents an Amenity

    Attributes:
        name (str): Name of amenity
    """

    name = ""
