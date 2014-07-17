import os
import ctypes

DIR = os.path.dirname(os.path.realpath(__file__))
LIBRARY_PATH = os.path.join(DIR, "libpersons.so")

class Person(ctypes.Structure):
    _fields_ = [
        ("name", ctypes.c_char_p),
        ("age", ctypes.c_int)
    ]


persons_handle = ctypes.cdll.LoadLibrary(LIBRARY_PATH)
persons_handle.get_person.restype = Person
person = persons_handle.get_person("Jordan", 21)

print("The name of the person is {} and the age is {}".format(person.name, person.age))
