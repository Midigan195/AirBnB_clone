#!/usr/bin/python3
"""
This module contains one class that serves as a base class.

This model serves as a base for other classes.
"""
from datetime import datetime
import uuid
import models


class BaseModel:
    """
    BaseModel serves as a base class for all other classes
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes id, created_at and updated_at attributes
        """
        if kwargs:
            for k, v in kwargs.items():
                if k != "__class__":
                    if k == "created_at" or k == "updated_at":
                        setattr(self, k, datetime.fromisoformat(v))
                    else:
                        setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Override the current string with formated string
        """
        string = "[{}] ({}) {}"
        return (string.format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """
        Update the attribute updated_at with current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary representation of instance
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = obj_dict['created_at'].isoformat()
        obj_dict['updated_at'] = obj_dict['updated_at'].isoformat()
        return obj_dict
