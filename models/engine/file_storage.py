#!/usr/bin/python3
""" Class FileStorage """

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    Class that serializes instances to
    a JSON file and deserializes JSON file to instances
    """
    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review}

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns dictionary of all saved objects """
        return self.__objects

    def new(self, obj):
        """ Sets in __objects the obj with key <obj class name>.id """
        new_key = f"{type(obj).__name__}.{obj.id}"
        self.__objects[new_key] = obj

    def save(self):
        """ Serializes __objects to the JSON file """
        json_dict = {}
        for key in self.__objects.keys():
            json_dict[key] = self.__objects[key].to_dict()
        with open(self.__file_path, "w", encoding="UTF-8") as write_file:
            json.dump(json_dict, write_file, indent=4)

    def reload(self):
        """ Deserializes the JSON file to __objects """
        try:
            with open(self.__file_path, "r") as read_file:
                j_o = json.load(read_file)
            for k in j_o:
                self.__objects[k] = self.classes[j_o[k]["__class__"]](**j_o[k])
        except FileNotFoundError:
            pass
