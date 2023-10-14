#!/usr/bin/python3
"""This defines a City class, inherites from basemodel"""
from models.base_model import BaseModel


class City(BaseModel):
    """Represents a City

    Attributes:
        state_id (str): it will be the State.id
        name (str): name of City
    """

    state_id = ""
    name = ""
