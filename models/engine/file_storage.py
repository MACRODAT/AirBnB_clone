#!/usr/bin/python3
"""
File storage data persist
"""

from datetime import datetime
import json
import os


class FileStorage:
    '''
    Storage class
    '''
    # file path
    __file_path = "persist.json"
    # objects
    __objects = {}

    def classes(self):
        """Returns a dictionary of classes for serialization"""
        from ..base_model import BaseModel  # noqa: 402
        from ..user import User  # noqa: 402
        from ..city import City  # noqa: 402
        from ..amenity import Amenity  # noqa: 402
        from ..place import Place  # noqa: 402
        from ..state import State  # noqa: 402
        from ..review import Review  # noqa: 402
        return {
            'BaseModel': BaseModel,
            'State': State,
            'Review': Review,
            'Amenity': Amenity,
            'Place': Place,
            'City': City,
            'User': User
            # Add other classes if needed
        }

    def all(self):
        """ returns the objects """
        return self.__objects

    def new(self, obj):
        """ appends a new file storage class """
        if obj is not None:
            self.__objects[f"{str(type(obj).__name__)}.{obj.id}"] = obj

    def save(self):
        """ serialization """
        dct = {}
        for k, o in self.__objects.items():
            dct[k] = o.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            data = json.dumps(dct)
            file.write(data)
            file.flush()

    def reload(self):
        """ refresh everything """
        nm = self.__file_path
        dct = {}
        self.__objects = {}
        if not os.path.exists(nm):
            return
        try:
            with open(nm, 'r', encoding='utf-8') as file:
                loaded = json.load(file)
            for k, v in loaded.items():
                class_name, _id = k.split('.')
                if class_name in self.classes():
                    obj_ = self.classes()[class_name](**v)
                    self.__objects[k] = obj_
        except e as Exception:
            pass
