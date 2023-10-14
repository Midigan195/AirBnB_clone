#!/usr/bin/python3
"""
This is the reviews class
"""
import models.base_model

class Review(models.base_model.BaseModel):
    """ THis class represents

    Attributes:
        place_id (str): this is the place.id
        user_id (str): this is the User.id
        text (str): this is the text string
    """

    place_id = ""
    user_id = ""
    text = ""
