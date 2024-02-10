import unittest
from models.base_model import BaseModel
import os
import json
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.base_model = BaseModel()

    def tearDown(self):
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_instance_attributes(self):
        self.assertTrue(hasattr(self.base_model, 'id'))
        self.assertTrue(hasattr(self.base_model, 'created_at'))
        self.assertTrue(hasattr(self.base_model, 'updated_at'))

    def test_instance_methods(self):
        self.assertTrue(hasattr(self.base_model, 'save'))
        self.assertTrue(hasattr(self.base_model, 'to_dict'))

    def test_id_is_string(self):
        self.assertIsInstance(self.base_model.id, str)

    def test_created_at_and_updated_at_are_datetime_objects(self):
        self.assertIsInstance(self.base_model.created_at, datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_save_updates_updated_at(self):
        old_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(old_updated_at, self.base_model.updated_at)

    def test_to_dict_returns_dict(self):
        model_dict = self.base_model.to_dict()
        self.assertIsInstance(model_dict, dict)

    def test_to_dict_contains_correct_keys_and_values(self):
        model_dict = self.base_model.to_dict()
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(
                model_dict['created_at'],
                self.base_model.created_at.isoformat())
        self.assertEqual(
                model_dict['updated_at'],
                self.base_model.updated_at.isoformat())

    def test_to_dict_has_all_attributes(self):
        model_dict = self.base_model.to_dict()
        self.assertIn('id', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)

    def test_str_representation(self):
        expected_str = "[BaseModel] ({}) {}".format(
                self.base_model.id, self.base_model.__dict__)
        self.assertEqual(str(self.base_model), expected_str)


if __name__ == '__main__':
    unittest.main()
