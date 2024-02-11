#!/usr/bin/python3
"""
Module for the FileStorage class.
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.city import City


class FileStorage:
    """
    FileStorage class for serializing and deserializing
    instances to/from a JSON file.
    """
    __file_path = "file.json"
    __objects = {
        "BaseModel": BaseModel,
        "User": User,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review,
        "State": State,
        "City": City
    }

    def all(self):
        """Returns the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        serialized_objects = {}
        for key, obj in FileStorage.__objects.items():
            serialized_objects[key] = obj.to_dict()
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                loaded_objects = json.load(file)
                for key, value in loaded_objects.items():
                    class_name, obj_id = key.split('.')
                    cls = eval(class_name)
                    instance = cls(**value)
                    FileStorage.__objects[key] = instance
        except FileNotFoundError:
            pass
