#!/usr/bin/python3
"""
    This is the entry point of the command interprter
"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User


class HBNBCommand(cmd.Cmd):
    """ The interpreter class """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """ This exits out of programme """
        return True

    def do_EOF(self, line):
        """ This exits out of programme when EOF detected """
        print("")
        return True

    def emptyline(self):
        """ detects an empty line and prints nothing """
        print

    def do_create(self, class_name):
        """ Creates a new instance of BaseModel """
        class_name = class_name.split()
        if len(class_name) == 0:
            print("** class name missing **")
        elif class_name[0] not in globals():
            print("** class doesn't exist **")
        else:
            print(eval(class_name[0])().id)
            storage.save()

    def do_show(self, arg):
        """ prints the string representation """
        arg = arg.split()
        dict_ob = storage.all()
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in globals():
            print("** class doesn't exist **")
        elif len(arg) < 2:
            print("** instance id missing **")
        elif "{}.{}".format(arg[0], arg[1]) not in dict_ob:
            print("** no instance found **")
        else:
            print(dict_ob["{}.{}".format(arg[0], arg[1])])

    def do_destroy(self, inst_name):
        """ Deletes an instance based on the class name and id """
        inst_name = inst_name.split()
        dict_obj = storage.all()
        if len(inst_name) == 0:
            print("** class name missing **")
        elif inst_name[0] not in globals():
            print("** class doesn't exist **")
        elif len(inst_name) < 2:
            print("** instance id missing **")
        elif "{}.{}".format(inst_name[0], inst_name[1]) not in dict_obj.keys():
            print("** no instance found **")
        else:
            del dict_obj["{}.{}".format(inst_name[0], inst_name[1])]
            storage.save()

    def do_all(self, arg):
        """ Prints the string representation of all class instances """
        arg = arg.split()
        if len(arg) > 0 and arg[0] not in globals():
            print("** class doesn't exist **")
        else:
            str_obj = []
            for str_ob in storage.all().values():
                if len(arg) > 0 and arg[0] == str_ob.__class__.__name__:
                    str_obj.append(str_ob.__str__())
                elif len(arg) == 0:
                    str_obj.append(str_ob.__str__())
            print(str_obj)

    def do_update(self, arg):
        """ Updates an instance based on the class name and id

            Usage: update <class name> <id> <attribute name>
                "<attribute value>"
        """
        arg = arg.split()
        dict_ob = storage.all()
        if len(arg) == 0:
            print("** class name missing **")
            return False
        if arg[0] not in globals():
            print("** class doesn't exist **")
            return False
        if len(arg) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(arg[0], arg[1]) not in dict_ob.keys():
            print("** no instance found **")
            return False
        if len(arg) == 2:
            print("** attribute name missing **")
            return False
        if len(arg) == 3:
            try:
                type(eval(arg[2])) != dict
            except NameError:
                print("** value missing **")
                return False
        if len(arg) == 4:
            ob = dict_ob["{}.{}".format(arg[0], arg[1])]
            if arg[2] in ob.__class__.__dict__.keys():
                value_typ = type(ob.__class__.__dict__[arg[2]])
                ob.__dict__[arg[2]] = value_typ(arg[3])
            else:
                ob.__dict__[arg[2]] = arg[3]

        elif type(eval(arg[2])) == dict:
            ob = dict_ob["{}.{}".format(arg[0], arg[1])]
            for key, value in eval(arg[2]).items():
                if (key in ob.__class__.__dict__.keys() and
                        type(ob.__class__.__dict__[key]) in {str, int, float}):
                    value_typ = type(ob.__class__.__dict__[key])
                    ob.__dict__[key] = value_typ(value)
                else:
                    ob.__dict__[key] = value
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
