#!/usr/bin/python3
""" Class HBNBCommand """

import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage
import shlex


class HBNBCommand(cmd.Cmd):
    """ Command line interpreter for AirBnB clone"""

    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review}

    prompt = '(hbnb) '

    def do_create(self, line):
        """creates an instance an save it on file.json"""
        if len(line) == 0:
            print("** class name missing **")
        elif line in self.classes.keys():
            new = self.classes[line]()
            new.save()
            print(new.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        """prints the str representation of an instance"""
        tokens = line.split()
        if len(tokens) == 0:
            print("** class name missing **")
        else:
            if tokens[0] in self.classes.keys():
                if len(tokens) == 1:
                    print("** instance id missing **")
                else:
                    objects = storage.all()
                    flag = None
                    for key in objects.keys():
                        if str(tokens[1]) in key:
                            flag = key
                    if flag:
                        print(objects[flag])
                    else:
                        print("** no instance found **")
            else:
                print("** class doesn't exist **")

    def do_destroy(self, line):
        """destroy an instance based on the class id"""
        tokens = line.split()
        if len(tokens) == 0:
            print("** class name missing **")
        else:
            if tokens[0] in self.classes.keys():
                if len(tokens) == 1:
                    print("** instance id missing **")
                else:
                    objects = storage.all()
                    flag = None
                    for key in objects.keys():
                        if str(tokens[1]) in key:
                            flag = key
                    if flag:
                        del(objects[flag])
                        storage.save()
                    else:
                        print("** no instance found **")
            else:
                print("** class doesn't exist **")

    def do_all(self, line=""):
        """prints all string representation of all instances"""
        objects = storage.all()
        list_objects = list()
        if line == "":
            for value in objects.values():
                list_objects.append(str(value))
            print(list_objects)
        elif line in self.classes.keys():
            for key, value in objects.items():
                if line in key:
                    list_objects.append(str(value))
            print(list_objects)
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """update an instance based on the class id"""
        tokens = shlex.split(line)
        integers = ['number_rooms', 'number_bathrooms',
                    'max_guest', 'price_by_night']
        floats = ['latitude', 'longitude']
        if len(tokens) == 0:
            print("** class name missing **")
        elif len(tokens) == 1 and tokens[0] in self.classes.keys():
            print("** instance id missing **")
        elif tokens[0] not in self.classes.keys():
            print("** class doesn't exist **")
        elif len(tokens) == 2:
            print("** attribute name missing **")
        elif len(tokens) == 3:
            print("** value missing **")
        else:
            objects = storage.all()
            flag = 0
            for k in objects.keys():
                if str(tokens[1]) in k:
                    if tokens[2] in integers:
                        tokens[3] = int(tokens[3])
                    elif tokens[2] in floats:
                        tokens[3] = float(tokens[3])
                    setattr(objects[k], tokens[2], tokens[3])
                    objects[k].save()
                    flag = 1
            if flag == 0:
                print("** no instance found **")

    def do_EOF(self, line):
        """ Exit the interpreter cleanly """
        print()
        return True

    def emptyline(self):
        """Called when an empty line is entered in response to the prompt.
        """
        if self.lastcmd:
            self.lastcmd = ""
            return self.onecmd('\n')

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_BaseModel(self, line):
        "Test"
        tokens = line.split(".")
        if tokens[1] == "all()":
            self.do_all("BaseModel")

    def do_User(self, line):
        """Test"""
        tokens = line.split(".")
        if tokens[1] == "all()":
            self.do_all("User")

    def do_State(self, line):
        """Test"""
        tokens = line.split(".")
        if tokens[1] == "all()":
            self.do_all("State")

    def do_City(self, line):
        """Test"""
        tokens = line.split(".")
        if tokens[1] == "all()":
            self.do_all("City")

    def do_Amenity(self, line):
        """Test"""
        tokens = line.split(".")
        if tokens[1] == "all()":
            self.do_all("Amenity")

    def do_Place(self, line):
        """Test"""
        tokens = line.split(".")
        if tokens[1] == "all()":
            self.do_all("Place")

    def do_Review(self, line):
        """Test"""
        tokens = line.split(".")
        if tokens[1] == "all()":
            self.do_all("Review")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
