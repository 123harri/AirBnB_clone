#!/usr/bin/python3
"""Defines unittests for models/engine/file_storage.py."""
import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        # Set up the environment before each test
        self.storage = FileStorage()
        self.model = BaseModel()

    def tearDown(self):
        # Clean up the environment after each test
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_all(self):
        # Test the all() method
        objects = self.storage.all()
        self.assertIsInstance(objects, dict)
        self.assertEqual(objects, {})

    def test_new(self):
        # Test the new() method
        self.storage.new(self.model)
        objects = self.storage.all()
        key = "{}.{}".format(self.model.__class__.__name__, self.model.id)
        self.assertIn(key, objects)

    def test_save_and_reload(self):
        # Test the save() and reload() methods
        self.storage.new(self.model)
        self.storage.save()

        # Check if the file is created
        self.assertTrue(os.path.exists("file.json"))

        # Reload the data and check if the object is present
        new_storage = FileStorage()
        new_storage.reload()
        objects_after_reload = new_storage.all()
        key = "{}.{}".format(self.model.__class__.__name__, self.model.id)
        self.assertIn(key, objects_after_reload)

    def test_reload_without_file(self):
        # Test reload() without an existing file
        self.storage.reload()
        # No exception should be raised


if __name__ == "__main__":
    unittest.main()
