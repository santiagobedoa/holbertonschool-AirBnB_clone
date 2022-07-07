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
import re


class HBNBCommand(cmd.Cmd):
    """ Command line interpreter for AirBnB clone"""

    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
        }

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
                    key = tokens[0] + "." + tokens[1]
                    if key in storage.all():
                        print(storage.all()[key])
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
                    key = tokens[0] + "." + tokens[1]
                    if key in storage.all():
                        storage.all().pop(key)
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
                    'max_guest', 'price_by_night', 'age']
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
        """Use: BaseModel.<method>() advanced task"""
        tokens = line.split(".")
        if tokens[1] == "all()":
            self.do_all("BaseModel")
        elif tokens[1] == "count()":
            count = 0
            for key in storage.all():
                if "BaseModel" in str(key):
                    count += 1
            print(count)
        elif tokens[1].find("show") != -1:
            class_id = (re.search('\"(.*)\"', tokens[1])).group(1)
            self.do_show(f"BaseModel {class_id}")
        elif tokens[1].find("destroy") != -1:
            class_id = (re.search('\"(.*)\"', tokens[1])).group(1)
            self.do_destroy(f"BaseModel {class_id}")
        elif tokens[1].find("update") != -1:
            expresion = (re.search(r'\((.*)\)', tokens[1])).group(1)
            if expresion.find("{") != -1:
                args = expresion.split(", ", 1)
                class_id = args[0].replace("\"", "")
                attrs = re.sub("{*'*\"*}*", '', args[1])
                attrs = dict(e.split(': ') for e in attrs.split(', '))
                for key, value in attrs.items():
                    self.do_update(f"BaseModel {class_id} {key} {value}")
            else:
                args = expresion.split(", ")
                args = [x.replace("\"", "") for x in args]
                self.do_update(f"BaseModel {args[0]} {args[1]} {args[2]}")

    def do_User(self, line):
        """Use: User.<method>() advanced task"""
        tokens = line.split(".")
        if tokens[1] == "all()":
            self.do_all("User")
        elif tokens[1] == "count()":
            count = 0
            for key in storage.all():
                if "User" in str(key):
                    count += 1
            print(count)
        elif tokens[1].find("show") != -1:
            class_id = (re.search('\"(.*)\"', tokens[1])).group(1)
            self.do_show(f"User {class_id}")
        elif tokens[1].find("destroy") != -1:
            class_id = (re.search('\"(.*)\"', tokens[1])).group(1)
            self.do_destroy(f"User {class_id}")
        elif tokens[1].find("update") != -1:
            expresion = (re.search(r'\((.*)\)', tokens[1])).group(1)
            if expresion.find("{") != -1:
                args = expresion.split(", ", 1)
                class_id = args[0].replace("\"", "")
                attrs = re.sub("{*'*\"*}*", '', args[1])
                attrs = dict(e.split(': ') for e in attrs.split(', '))
                for key, value in attrs.items():
                    self.do_update(f"User {class_id} {key} {value}")
            else:
                args = expresion.split(", ")
                args = [x.replace("\"", "") for x in args]
                self.do_update(f"User {args[0]} {args[1]} {args[2]}")

    def do_State(self, line):
        """Use: State.<method>() advanced task"""
        tokens = line.split(".")
        if tokens[1] == "all()":
            self.do_all("State")
        elif tokens[1] == "count()":
            count = 0
            for key in storage.all():
                if "State" in str(key):
                    count += 1
            print(count)
        elif tokens[1].find("show") != -1:
            class_id = (re.search('\"(.*)\"', tokens[1])).group(1)
            self.do_show(f"State {class_id}")
        elif tokens[1].find("destroy") != -1:
            class_id = (re.search('\"(.*)\"', tokens[1])).group(1)
            self.do_destroy(f"State {class_id}")
        elif tokens[1].find("update") != -1:
            expresion = (re.search(r'\((.*)\)', tokens[1])).group(1)
            if expresion.find("{") != -1:
                args = expresion.split(", ", 1)
                class_id = args[0].replace("\"", "")
                attrs = re.sub("{*'*\"*}*", '', args[1])
                attrs = dict(e.split(': ') for e in attrs.split(', '))
                for key, value in attrs.items():
                    self.do_update(f"State {class_id} {key} {value}")
            else:
                args = expresion.split(", ")
                args = [x.replace("\"", "") for x in args]
                self.do_update(f"State {args[0]} {args[1]} {args[2]}")

    def do_City(self, line):
        """Use: City.<method>() advanced task"""
        tokens = line.split(".")
        if tokens[1] == "all()":
            self.do_all("City")
        elif tokens[1] == "count()":
            count = 0
            for key in storage.all():
                if "City" in str(key):
                    count += 1
            print(count)
        elif tokens[1].find("show") != -1:
            class_id = (re.search('\"(.*)\"', tokens[1])).group(1)
            self.do_show(f"City {class_id}")
        elif tokens[1].find("destroy") != -1:
            class_id = (re.search('\"(.*)\"', tokens[1])).group(1)
            self.do_destroy(f"City {class_id}")
        elif tokens[1].find("update") != -1:
            expresion = (re.search(r'\((.*)\)', tokens[1])).group(1)
            if expresion.find("{") != -1:
                args = expresion.split(", ", 1)
                class_id = args[0].replace("\"", "")
                attrs = re.sub("{*'*\"*}*", '', args[1])
                attrs = dict(e.split(': ') for e in attrs.split(', '))
                for key, value in attrs.items():
                    self.do_update(f"City {class_id} {key} {value}")
            else:
                args = expresion.split(", ")
                args = [x.replace("\"", "") for x in args]
                self.do_update(f"City {args[0]} {args[1]} {args[2]}")

    def do_Amenity(self, line):
        """Use: Amenity.<method>() advanced task"""
        tokens = line.split(".")
        if tokens[1] == "all()":
            self.do_all("Amenity")
        elif tokens[1] == "count()":
            count = 0
            for key in storage.all():
                if "Amenity" in str(key):
                    count += 1
            print(count)
        elif tokens[1].find("show") != -1:
            class_id = (re.search('\"(.*)\"', tokens[1])).group(1)
            self.do_show(f"Amenity {class_id}")
        elif tokens[1].find("destroy") != -1:
            class_id = (re.search('\"(.*)\"', tokens[1])).group(1)
            self.do_destroy(f"Amenity {class_id}")
        elif tokens[1].find("update") != -1:
            expresion = (re.search(r'\((.*)\)', tokens[1])).group(1)
            if expresion.find("{") != -1:
                args = expresion.split(", ", 1)
                class_id = args[0].replace("\"", "")
                attrs = re.sub("{*'*\"*}*", '', args[1])
                attrs = dict(e.split(': ') for e in attrs.split(', '))
                for key, value in attrs.items():
                    self.do_update(f"Amenity {class_id} {key} {value}")
            else:
                args = expresion.split(", ")
                args = [x.replace("\"", "") for x in args]
                self.do_update(f"Amenity {args[0]} {args[1]} {args[2]}")

    def do_Place(self, line):
        """Use: Place.<method>() advanced task"""
        tokens = line.split(".")
        if tokens[1] == "all()":
            self.do_all("Place")
        elif tokens[1] == "count()":
            count = 0
            for key in storage.all():
                if "Place" in str(key):
                    count += 1
            print(count)
        elif tokens[1].find("show") != -1:
            class_id = (re.search('\"(.*)\"', tokens[1])).group(1)
            self.do_show(f"Place {class_id}")
        elif tokens[1].find("destroy") != -1:
            class_id = (re.search('\"(.*)\"', tokens[1])).group(1)
            self.do_destroy(f"Place {class_id}")
        elif tokens[1].find("update") != -1:
            expresion = (re.search(r'\((.*)\)', tokens[1])).group(1)
            if expresion.find("{") != -1:
                args = expresion.split(", ", 1)
                class_id = args[0].replace("\"", "")
                attrs = re.sub("{*'*\"*}*", '', args[1])
                attrs = dict(e.split(': ') for e in attrs.split(', '))
                for key, value in attrs.items():
                    self.do_update(f"Place {class_id} {key} {value}")
            else:
                args = expresion.split(", ")
                args = [x.replace("\"", "") for x in args]
                self.do_update(f"Place {args[0]} {args[1]} {args[2]}")

    def do_Review(self, line):
        """Use: Review.<method>() advanced task"""
        tokens = line.split(".")
        if tokens[1] == "all()":
            self.do_all("Review")
        elif tokens[1] == "count()":
            count = 0
            for key in storage.all():
                if "Review" in str(key):
                    count += 1
            print(count)
        elif tokens[1].find("show") != -1:
            class_id = (re.search('\"(.*)\"', tokens[1])).group(1)
            self.do_show(f"Review {class_id}")
        elif tokens[1].find("destroy") != -1:
            class_id = (re.search('\"(.*)\"', tokens[1])).group(1)
            self.do_destroy(f"Review {class_id}")
        elif tokens[1].find("update") != -1:
            expresion = (re.search(r'\((.*)\)', tokens[1])).group(1)
            if expresion.find("{") != -1:
                args = expresion.split(", ", 1)
                class_id = args[0].replace("\"", "")
                attrs = re.sub("{*'*\"*}*", '', args[1])
                attrs = dict(e.split(': ') for e in attrs.split(', '))
                for key, value in attrs.items():
                    self.do_update(f"Review {class_id} {key} {value}")
            else:
                args = expresion.split(", ")
                args = [x.replace("\"", "") for x in args]
                self.do_update(f"Review {args[0]} {args[1]} {args[2]}")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
