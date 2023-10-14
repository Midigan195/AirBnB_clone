#!/usr/bin/python3
"""
This is the Place class
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """ Represents a place

    Attributes:
        city_id (str): this is the city.id
        user_id (str): will be the User.id
        name (str): empty string
        description (str): empty string
        number_rooms (int): the number of rooms
        number_bathrooms (int): number of bathrooms
        max_guest (int): maximum amount of guests
        price_by_night (int): the price per night
        latitude (float): latitude of place
        longitude (float): longitude of place
        amenity_ids (str): will be the list of Amenity.id later
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
