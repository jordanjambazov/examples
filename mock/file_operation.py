import os

def baba(file_name):
    if os.path.exists(file_name):
        f = open(file_name, "w+")
        f.write("test")
        f.close()
    else:
        raise Exception
