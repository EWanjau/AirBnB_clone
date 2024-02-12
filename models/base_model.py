#!/usr/bin/python3
"""
Main classs that will inherit
"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """ defines all common attributes/methods
    """
    def __init__(self, *args, **kwargs):
        """ initializes attributes
        """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)
        else:
            ft = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(kwargs[key], ft)
                if key != '__class__':
                    setattr(self, key, value)

    def __str__(self):
        """ return class name, id, attr
        """
        class_name = "[" + self.__class__.__name__ + "]"
        attr = {k: v for (k, v) in self.__dict__.items() if (not v) is False}
        return class_name + " (" + self.id + ") " + str(attr)

    def save(self):
        """ updates with current datetime
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ create a new dict and return
        """
        new_dict = {}

        for key, values in self.__dict__.items():
            if key == 'created_at' or key == 'updated_at':
                new_dict[key] = values.strftime("%Y-%m-%dT%H:%M:%S.%f")
            else:
                if not values:
                    pass
                else:
                    new_dict[key] = values
        new_dict['__class__'] = self.__class__.__name__

        return new_dict
