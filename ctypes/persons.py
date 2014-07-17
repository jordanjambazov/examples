import os
import ctypes

DIR = os.path.dirname(__file__)
LIBRARY_PATH = os.path.join(DIR, "libpersons.so")

class Person(ctypes.Structure):
    _fields_ = [
        ("name", ctypes.c_char_p),
        ("age", ctypes.c_int)
    ]


class PersonProxy(object):
    def __init__(self):
        self.handle = ctypes.cdll.LoadLibrary(LIBRARY_PATH)
        self.handle.get_person.restype = Person

    def get_person(self, name, age):
        person = self.handle.get_person(name, age)
        return person

