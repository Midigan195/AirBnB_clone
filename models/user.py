#!/usr/bin/python3
"""This module defines a class that is a representation of a user."""
from models.base_model import BaseModel


class User(BaseModel):
    """This class represents a specific user.

    Attributes:
        email (string): This is the user email.
        password (string): This is the password of user.
        first_name (string): This is first name of user.
        last_name (string): This is the surname of user.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
