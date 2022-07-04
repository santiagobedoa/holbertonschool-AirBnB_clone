#!/usr/bin/python3
""" Class HBNBCommand """

import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """ Command line interpreter for AirBnB clone"""

    prompt = '(hbnb) '

    def do_create(self, line):
        if len(line) == 0:
            print("** class name missing **")
        elif line == 'BaseModel':
            new = BaseModel()
            new.save()
            print(new.id)
        else:
            print("** class doesn't exist **")

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
