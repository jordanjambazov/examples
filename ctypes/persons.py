import ctypes


class Person(ctypes.Structure):
    _fields_ = [
        ("name", ctypes.c_char_p),
        ("age", ctypes.c_int)
    ]


persons_handle = ctypes.cdll.LoadLibrary("/home/jordan/Sandbox/Persons/libperson.so")

person = persons_handle.get_person("Jordan", 21)
