#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_name(self, name):
        if type(name) == str and 1 <= len(name) <= 25:
            self._name = name.title()
        else:
            print("Name must be string between 1 and 25 characters.")

    name = property(get_name, set_name)

    # def __init__(self, name):
    #     self._name = name

    # def get_name(self):
    #     return self._name
    
    # def set_name(self, name):
    #     if (type(name) in (str) and (1<= name <= 25)):
    #         print(self.name)
    #     else:
    #         print("Name must be string between 1 and 25 characters.")
    # name = property(set_name, get_name)

    # def __init__(self, name):
    #     self._name = name
    
    # @property
    # def name(self):
    #     return self._name
    
    # @name.setter
    # def name(self, value):
    #     if not isinstance(value, str) or not 1 <= len(value) <= 25:
    #         print("Name must be string between 1 and 25 characters.")
    #     else:
    #         self._name = value