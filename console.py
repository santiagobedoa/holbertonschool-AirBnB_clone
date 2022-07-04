#!/usr/bin/python3
""" Class HBNBCommand """

import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """ Command line interpreter for AirBnB clone"""

    prompt = '(hbnb) '

    def do_create(self, line):
        """creates an instance an save it on file.json"""
        if len(line) == 0:
            print("** class name missing **")
        elif line == 'BaseModel':
            new = BaseModel()
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
            if tokens[0] == "BaseModel":
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
            if tokens[0] == "BaseModel":
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
        if line != "" and line != "BaseModel":
            print("** class doesn't exist **")
        else:
            objects = storage.all()
            list_objs = list()
            for key, value in objects.items():
                list_objs.append(str(value))
            print(list_objs)

    def do_update(self, line):
        tokens = line.split()
        if len(tokens) == 0:
            print("** class name missing **")
        elif len(tokens) == 1 and tokens[0] == 'BaseModel':
            print("** instance id missing **")
        elif tokens[0] != 'BaseModel':
            print("** class doesn't exist **")
        elif len(tokens) == 2:
            print("** attribute name missing **")
        elif len(tokens) == 3:
            print("** value missing **")
        else:
            objects = storage.all()
            for key in objects.keys():
                if str(tokens[1]) in key:
                    print(objects[key])
                    setattr(objects[key], tokens[2], tokens[3])
                    objects[key].save()
                    print(objects[key])
                else:
                    print("** no instance found **")

    def do_EOF(self, line):
        """ Exit the interpreter cleanly """
        print()
        return True

    def empty_line(self):
        """ Upon empty line, do nothing """
        pass

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
