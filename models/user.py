#!/usr/bin/python3
"""This module defines a class that is a representation of a user"""
from models.base_model import BaseModel


class User(BaseModel):
    """This class represents a specific user.

    Attributes:
        email (string): User email
        password (string): Password of user
        first_name (string): First name of user
        last_name (string): Surname of user
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
