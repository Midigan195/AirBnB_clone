#!/usr/bin/python3
"""
This module defines a class that defines a file storage engine
"""
import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """
    File storage serialises and deserialises instances to a json file
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Sets object with the classname and id
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serialises __objects to Json file
        """
        data = {}
        for key, value in FileStorage.__objects.items():
            data[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(data, file)

    def reload(self):
        """
        Deserialises the json file to __objects
        """
        try:
            with open(FileStorage.__file_path) as f:
                    objdict = json.load(f)
                    for obj in objdict.values():
                        cls_name = obj["__class__"]
                        del obj["__class__"]
                        self.new(eval(cls_name)(**obj))
        except FileNotFoundError:
            pass
