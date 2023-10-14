#!/usr/bin/python3
"""
Defines unittest for the File storage module
"""
import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.amenity import Amenity
from models.review import Review
from models.city import City


class TestFileStorage(unittest.TestCase):
    """
    Creates a test suite for Filestorage
    """
    def setUp(self):
        """
        Setup a filestorage instance
        """
        file_path = FileStorage._FileStorage__file_path
        if os.path.exists(file_path):
            os.remove(file_path)
        self.storage = FileStorage()

    def tearDown(self):
        """
        Tear down File storage instance
        """
        if self.storage is not None:
            self.storage = None

    def test_file_storage_attrs(self):
        """
        Test class attributes of filestorage
        """
        storage = FileStorage()
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))
        with self.assertRaises(AttributeError):
            path = storage.__file_path
        with self.assertRaises(AttributeError):
            path = storage.__objects

    def test_file_storage_all(self):
        """
        Test file storage all with different classes
        """
        self.storage = FileStorage()

        base_model = BaseModel()
        user = User()
        place = Place()
        state = State()
        amenity = Amenity()
        review = Review()
        city = City()

        self.storage.new(base_model)
        self.storage.new(user)
        self.storage.new(place)
        self.storage.new(state)
        self.storage.new(amenity)
        self.storage.new(review)
        self.storage.new(city)

        all_objects = self.storage.all()
        self.assertIn("User.{}".format(user.id), all_objects)
        self.assertIn("BaseModel.{}".format(base_model.id), all_objects)
        self.assertIn("Place.{}".format(place.id), all_objects)
        self.assertIn("State.{}".format(state.id), all_objects)
        self.assertIn("Amenity.{}".format(amenity.id), all_objects)
        self.assertIn("Review.{}".format(review.id), all_objects)
        self.assertIn("City.{}".format(city.id), all_objects)

    def test_file_storage_save_and_reload(self):
        """
        Test file storage save and reload for different classes
        """
        self.storage = FileStorage()

        base_model = BaseModel()
        user = User()
        place = Place()
        state = State()
        amenity = Amenity()
        review = Review()
        city = City()

        self.storage.new(base_model)
        self.storage.new(user)
        self.storage.new(place)
        self.storage.new(state)
        self.storage.new(amenity)
        self.storage.new(review)
        self.storage.new(city)

        self.storage.save()

        new_storage = FileStorage()
        new_storage.reload()

        self.assertEqual(new_storage.all(), self.storage.all())

    def test_file_storage_update(self):
        """
        Test file storage Update
        """
        self.storage = FileStorage()
        place = Place()
        self.storage.new(place)
        place.name = "Updated Place Name"

        self.storage.save()

        new_storage = FileStorage()
        new_storage.reload()
        updated_place = new_storage.all()["Place.{}".format(place.id)]
        self.assertEqual(updated_place.name, "Updated Place Name")

        self.storage = FileStorage()
        city = City()
        self.storage.new(city)
        city.name = "Updated City Name"

        self.storage.save()

        new_storage = FileStorage()
        new_storage.reload()
        updated_city = new_storage.all()["City.{}".format(city.id)]
        self.assertEqual(updated_city.name, "Updated City Name")

        self.storage = FileStorage()
        amenity = Amenity()
        self.storage.new(amenity)
        amenity.name = "Updated Amenity Name"

        self.storage.save()

        new_storage = FileStorage()
        new_storage.reload()
        updated_amenity = new_storage.all()["Amenity.{}".format(amenity.id)]
        self.assertEqual(updated_amenity.name, "Updated Amenity Name")

        self.storage = FileStorage()
        state = State()
        self.storage.new(state)
        state.name = "Updated State Name"

        self.storage.save()

        new_storage = FileStorage()
        new_storage.reload()
        updated_state = new_storage.all()["State.{}".format(state.id)]
        self.assertEqual(updated_state.name, "Updated State Name")

        self.storage = FileStorage()
        review = Review()
        self.storage.new(review)
        review.name = "Updated Review Name"

        self.storage.save()

        new_storage = FileStorage()
        new_storage.reload()
        updated_review = new_storage.all()["Review.{}".format(review.id)]
        self.assertEqual(updated_review.name, "Updated Review Name")

    def test_file_storage_non_existent_json_file(self):
        """
        Test file storage with a non existing json file
        """
        FileStorage.__file_path = "new.json"
        prev = self.storage.all()
        self.storage.reload()
        self.assertEqual(self.storage.all(), prev)

    def test_file_storage_empty_json_file(self):
        """
        Test file storage with empty file
        """
        FileStorage.__file_path = "Another.json"
        prev = self.storage.all()
        self.storage.reload()
        self.assertEqual(self.storage.all(), prev)
