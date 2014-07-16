Reading structure from C library
================================

The purpose of this example is to illustrate how to read C structure when calling external library. It was not well documented anywhere.

*How to compile the C library*
    gcc -c -fPIC persons.c -o persons.o
    gcc persons.o -shared -o libpersons.so
