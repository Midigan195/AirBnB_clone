#!/usr/bin/python3
"""This is a state class inheriting from BaseModel"""
from models.base_model import BaseModel


class State(BaseModel):
    """Representation of a state

    Attributes:
        name (str): empty string
    """

    name = ""
