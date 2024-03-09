#!/usr/bin/python3

"""
Module contains class HBNBCommand that runs the program's front end
"""

import cmd
import sys
import re
import ast
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.amenity import Amenity
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Class defines an interative shell
    """

    prompt = "(hbnb) "
    CLS = ["BaseModel", "User", "Amenity", "State", "City", "Place", "Review"]

    def precmd(self, line):
        """
        Modify the input line before execution
        """
        if not sys.stdin.isatty():
            print()
        if '.' in line:
            parts = line.split('.')
            if len(parts) >= 2:
                _clas_meth, args = parts[0], '.'.join(parts[1:])
                clas, meth = _clas_meth.strip(), args.split('(', 1)[0].strip()
                args = args.split('(', 1)[1].rsplit(')', 1)[0].strip()
                args = args.strip("'")
                args = args.strip('"')
                if clas not in HBNBCommand.CLS:
                    print("** class doesn't exist **")
                else:
                    line = f"{meth} {clas} {args}"
            else:
                print("** Invalid syntax: Class or method missing **")
        return cmd.Cmd.precmd(self, line)

    def do_quit(self):
        """
        Quits the Console
        """
        return True

    def do_EOF(self, line):
        """
        Quits the Console
        """
        print("")
        return True

    def do_create(self, line):
        """
        Creates an instance of BaseModel

        Parameters:
        line (str): string that comes after command 'create'
        """
        if len(line) == 0 or line is None:
            print("** class name missing **")
        else:
            if line in HBNBCommand.CLS:
                obj = eval(line)()
                print(obj.id)
                obj.save()
            else:
                print("** class doesn't exist **")

    def do_show(self, line):
        """
        Prints str representation of an instance

        Parameters:
        line (str): string after command that contains class and id
        """
        if len(line) == 0:
            print("** class name is missing **")
            return
        else:
            argu = line.split()
            if argu[0] in HBNBCommand.CLS:
                if len(argu) < 2:
                    print("** instance id missing **")
                elif f"{argu[0]}.{argu[1]}" in storage.all().keys():
                    print(storage.all()[f"{argu[0]}.{argu[1]}"])
                else:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")

    def do_destroy(self, line):
        """
        Deletes instance based on class name and id

        Parameters:
        line (str): string after command that contains class and id
        """
        argu = line.split()
        if len(line) == 0:
            print("** class name is missing **")
        else:
            if argu[0] in HBNBCommand.CLS:
                if len(argu) < 2:
                    print("** instance id missing **")
                elif f"{argu[0]}.{argu[1]}" in storage.all().keys():
                    del storage.all()[f"{argu[0]}.{argu[1]}"]
                    storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")

    def do_all(self, line):
        """
        Prints string representations of all istances of a class

        Parameters:
        line (str): string after command contaning the class name
        """
        _all = list()
        if line in HBNBCommand.CLS:
            for k, v in storage.all().items():
                _class, _id = k.split('.')
                if _class == line:
                    _all.append(v.__str__())
            print(f"{_all}")
        else:
            print("** class doesn't exist **")

    def do_count(self, line):
        """
        Returns number of instances of said class

        Parameters:
        line (str): string contaning class
        """
        count = 0
        if line in HBNBCommand.CLS:
            for k, v in storage.all().items():
                _class, _id = k.split('.')
                if _class == line:
                    count = count + 1
            print(count)
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """
        Updates an instance based on class name and id

        Parameters:
        line (str): contains the object, attribute and id
        """
        prohibited = ["id", "created_at", "updated_at"]
        if len(line) == 0:
            print("** class name is missing **")
            return
        if '{' in line:
            clas_id, _dict = line.split(',', 1)
            clas, _id = clas_id.split()
            _id = _id.strip()
            _id = _id.strip('"')
            _id = _id.strip("'")
            clas = clas.strip()
            if clas not in HBNBCommand.CLS:
                print("** class doesn't exist **")
                return
            if ("{}.{}".format(clas, _id)) not in storage.all().keys():
                print("** no instance found **")
                return
            dict_str = re.search('({.+})', _dict).group(0)
            dict_ob = ast.literal_eval(dict_str)
            if len(dict_ob) == 0 or dict_ob is None:
                print("** attribute name missing **")
            key = "{}.{}".format(clas, _id)
            for item in dict_ob.keys():
                if item not in prohibited:
                    big_dict = storage.all()
                    setattr(big_dict[key], item, dict_ob[item])
                    storage.save()
        else:
            args = line.split()
            if len(args) >= 4:
                key = "{}.{}".format(args[0], args[1])
                cast = type(eval(args[3]))
                arg3 = args[3]
                arg3 = arg3.strip('"')
                arg3 = arg3.strip("'")
                if args[2] not in prohibited:
                    big_dict = storage.all()
                    setattr(big_dict[key], args[2], cast(arg3))
                    storage.save()
            elif len(args) == 0:
                print("** class name missing **")
            elif args[0] not in HBNBCommand.CLS:
                print("** class doesn't exist **")
            elif len(args) == 1:
                print("** instance id missing **")
            elif "{}.{}".format(args[0], args[1]) not in storage.all().keys():
                print("** no instance found **")
            elif len(args) == 2:
                print("** attribute name missing **")
            else:
                print("** value missing **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
