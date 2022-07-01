""" Classs FileStorage """
import json


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
        json.dump(json_dict, write_file)


def reload(self):
    """ Deserializes the JSON file to __objects """
    try:
        with open(self.__file_path, "r") as read_file:
            py_obj = json.load(read_file)
    except FileNotFoundError:
        pass
