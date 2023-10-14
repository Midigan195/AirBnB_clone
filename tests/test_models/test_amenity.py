import unittest
import uuid
import json
from datetime import datetime
from models.amenity import Amenity
"""
Define a test class for Amenity
"""


class TestAmenity(unittest.TestCase):
    """
    Define a list of test suites for Amenity
    """

    def test_id_isstring(self):
        """
        Test that id is a string
        """
        obj = Amenity()
        self.assertIsInstance(obj.id, str)

    def test_id_unique(self):
        """
        Test that each id is unique
        """
        obj1 = Amenity()
        obj2 = Amenity()
        self.assertNotEqual(obj1.id, obj2.id)

    def test_uneqaul_created_and_updated(self):
        """
        Test that created_at and updated_at values are different
        for each instance
        """
        obj1 = Amenity()
        obj2 = Amenity()
        self.assertNotEqual(obj1.created_at, obj2.created_at)
        self.assertNotEqual(obj1.updated_at, obj2.updated_at)

    def test_nomrmal_str(self):
        """
        Test __str__ method with a normal case of Amenity
        """
        obj = Amenity()
        expected_str = f"[{obj.__class__.__name__}] ({obj.id}) {obj.__dict__}"
        self.assertEqual(str(obj), expected_str)

    def test_str_with_custom_attr(self):
        """
        Test __str__ method with a custom attribute
        """
        obj = Amenity()
        obj.custom_attr = "custom_value"
        self.assertEqual("custom_value", obj.__dict__['custom_attr'])

    def test_set_attr(self):
        """
        Test __str__ with attributes set
        """
        obj = Amenity()
        obj.created_at = datetime(2022, 1, 1, 0, 0, 0)
        obj.updated_at = datetime(2022, 2, 2, 0, 0, 0)
        obj.id = "test_id"
        expected_output = (
                "[Amenity] (test_id) {'id': 'test_id', "
                "'created_at': datetime.datetime(2022, 1, 1, 0, 0), "
                "'updated_at': datetime.datetime(2022, 2, 2, 0, 0)}"
        )
        self.assertEqual(str(obj), expected_output)

    def test_save_update(self):
        """
        Test that save changes the update_at attribute
        """
        obj = Amenity()
        initial_update = obj.updated_at
        obj.save()
        updated_update = obj.updated_at
        self.assertNotEqual(initial_update, updated_update)

    def test_save_created(self):
        """
        Test that save does not change the created_at attribute
        """
        obj = Amenity()
        initial_create = obj.created_at
        obj.save()
        updated_create = obj.created_at
        self.assertEqual(initial_create, updated_create)

    def test_to_dict_normal(self):
        """
        Test to_dict with a normal case
        """
        amenity = Amenity()
        obj_dict = amenity.to_dict()
        self.assertEqual(len(obj_dict), 4)
        self.assertIn('__class__', obj_dict)
        self.assertIn('id', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)

    def test_to_dict_type_is_dict(self):
        """
        Test that return value of to dict is a dictionary
        """
        obj = Amenity()
        self.assertTrue(dict, type(obj.to_dict))

    def test_to_dict_class_name(self):
        """
        Test if to_dict contains the right class name
        """
        amenity = Amenity()
        obj_dict = amenity.to_dict()
        self.assertEqual(obj_dict['__class__'], 'Amenity')

    def test_to_dict_id_format(self):
        """
        Test if id is in uuid format
        """
        amenity = Amenity()
        obj_dict = amenity.to_dict()
        self.assertTrue(uuid.UUID(obj_dict['id'], version=4))

    def test_to_dict_valid_json(self):
        """
        Test if dictionary is in valid json format
        """
        amenity = Amenity()
        obj_dict = amenity.to_dict()
        json_str = json.dumps(obj_dict)
        loaded_dict = json.loads(json_str)
        self.assertEqual(obj_dict, loaded_dict)

    def test_to_dict_iso_format(self):
        """
        Test if created_at and updated_at is in iso_fomat
        """
        amenity = Amenity()
        obj_dict = amenity.to_dict()
        self.assertEqual(len(obj_dict['created_at']), 26)
        self.assertEqual(len(obj_dict['updated_at']), 26)

    def test_to_dict_with_added_attrs(self):
        """
        Test if dictionary works for added attributes
        """
        amenity = Amenity()
        amenity.name = "Jeffry"
        amenity.surname = "Bezos"
        self.assertIn("name", amenity.to_dict())
        self.assertIn("surname", amenity.to_dict())
        self.assertEqual("Jeffry", amenity.to_dict()["name"])
        self.assertEqual("Bezos", amenity.to_dict()["surname"])

    def test_kwargs_normal(self):
        """
        Test when kwargs is a normal dictionary
        """
        data = {
            '__class__': 'Amenity',
            'id': 'some_id_value',
            'created_at': '2023-10-12T12:00:00',
            'updated_at': '2023-10-12T12:30:00'
        }
        obj = Amenity(**data)
        self.assertEqual(obj.id, 'some_id_value')
        self.assertEqual(obj.created_at, datetime(2023, 10, 12, 12, 0, 0))
        self.assertEqual(obj.updated_at, datetime(2023, 10, 12, 12, 30, 0))
        self.assertNotIn("__class__", obj.__dict__)

    def test_kwargs_extra_attrs(self):
        """
        Test when kwargs has extra attributes
        """
        data = {
            'id': 'some_id_value',
            'created_at': '2023-10-12T12:00:00',
            'updated_at': '2023-10-12T12:30:00',
            'name': 'John'
        }
        obj = Amenity(**data)
        self.assertEqual(obj.id, 'some_id_value')
        self.assertEqual(obj.created_at, datetime(2023, 10, 12, 12, 0, 0))
        self.assertEqual(obj.updated_at, datetime(2023, 10, 12, 12, 30, 0))
        self.assertIn('name', obj.__dict__)
        self.assertEqual(obj.name, 'John')

    def test_kwargs_Empty_dict(self):
        """
        Test when kwargs is empty
        """
        data = {}
        obj = Amenity(**data)
        self.assertEqual(len(obj.__dict__), 3)

    def test_kwargs_None(self):
        """
        Test when kwargs is None
        """
        data = None
        obj = Amenity(data)
        self.assertEqual(len(obj.__dict__), 3)

    def test_kwargs_Not_dict(self):
        """
        Test when kwargs is not a dictioanry
        """
        data = [1, 4, 8]
        obj = Amenity(data)
        self.assertEqual(len(obj.__dict__), 3)

    def test_class_attrs(self):
        """
        Test that class attributes are set
        """
        name = Amenity.name
        self.assertEqual("", name)
