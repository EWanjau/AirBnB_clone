#!/usr/bin/python3
"""
entry point of the command interpreter
"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.review import Review
from models.amenity import Amenity
import json
import shlex


class HBNBCommand(cmd.Cmd):
    """ command interpreter
    """
    prompt = "(hbnb) "
    classname = ['BaseModel', 'User', 'Place', 'Amenity', 'City',
                 'State', 'Review']
    l_cls = ['show', 'create', 'destroy', 'update', 'all']

    def precmd(self, arg):
        """ parses command input """
        if '.' in arg and '(' in arg and ')' in arg:
            cls = arg.split('.')
            cnd = cls[1].split('(')
            args = cnd[1].split(')')
            if cls[0] in HBNBCommand.classname and cnd[0] in HBNBCommand.l_cls:
                arg = cnd[0] + ' ' + cls[0] + ' ' + args[0]
        return arg

    def do_quit(self, line):
        """ quit command """
        return True

    def do_EOF(self, line):
        """ EOF command """
        return True

    def emptyline(self):
        """ do nothing """
        pass

    def do_create(self, arg):
        """ creates a new instance of BaseModel """

        if not arg:
            print("** class name missing **")
        elif arg not in HBNBCommand.classname:
            print("** class doesn't exist **")
        else:
            dct = {'BaseModel': BaseModel}
            my_model = dct[arg]()
            print(my_model.id)
            my_model.save()

    def do_show(self, arg):
        """ show string representation of an instance """

        if not arg:
            print("** class name missing **")
            return

        args = arg.split(' ')

        if args[0] not in HBNBCommand.classname:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            objs = storage.all()
            for key, value in objs.items():
                obj_name = value.__class__.__name__
                obj_id = value.id
                if obj_name == args[0] and obj_id == args[1].strip('"'):
                    print(value)
                    return
            print("** no instance found **")

    def do_destroy(self, arg):
        """ delete an instance """

        if not arg:
            print("** class name missing **")
            return

        args = arg.split(' ')

        if args[0] not in HBNBCommand.classname:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            objs = storage.all()
            for key, value in objs.items():
                obj_name = value.__class__.__name__
                obj_id = value.id
                if obj_name == args[0] and obj_id == args[1].strip('"'):
                    del value
                    del storage._FileStorage__objects[key]
                    storage.save()
                    return
            print("** no instance found **")

    def do_all(self, arg):
        """ print all string representation of all instance """

        if not arg:
            print("** class name missing **")
            return

        args = arg.split(' ')

        if args[0] not in HBNBCommand.classname:
            print("** class doesn't exist **")
        else:
            objs = storage.all()
            list_inst = []
            for key, value in objs.items():
                obj_name = value.__class__.__name__
                if obj_name == args[0]:
                    list_inst += [value.__str__()]
            print(list_inst)

    def do_update(self, arg):
        """ update attribute """

        if not arg:
            print("** class name missing **")
            return

        a = ""
        for argv in arg.split(','):
            a = a + argv

        args = shlex.split(a)

        if args[0] not in HBNBCommand.classname:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            objs = storage.all()
            for key, objc in objs.items():
                obj_name = objc.__class__.__name__
                obj_id = objc.id
                if obj_name == args[0] and obj_id == args[1].strip('"'):
                    if len(args) == 2:
                        print("** attribute name missing **")
                    elif len(args) == 3:
                        print("** value missing **")
                    else:
                        setattr(objc, args[2], args[3])
                        storage.save()
                    return

            print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
