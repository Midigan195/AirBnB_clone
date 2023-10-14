#!/usr/bin/python3
"""This is the reviews class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """THis class represents a Review.

    Attributes:
        place_id (str): this is the place.id.
        user_id (str): this is the User.id.
        text (str): this is the text string.
    """

    place_id = ""
    user_id = ""
    text = ""
