#!/usr/bin/python3
""" Class FileStorage """

import json
from models.base_model import BaseModel
from models.user import User

classes = {"BaseModel": BaseModel, "User": User}

class FileStorage:
    """
    Class that serializes instances to
    a JSON file and deserializes JSON file to instances
    """

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
                json_obj = json.load(read_file)
            for key in json_obj:
                self.__objects[key] = classes[json_obj[key]["__class__"]](**json_obj[key])
        except FileNotFoundError:
            pass
