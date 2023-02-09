import os

from simple import hello_world


def read_from_file(filename):
    if not os.path.exists(filename):
        raise Exception("Bad File")
    infile = open(filename, "r")
    line = infile.readline()
    return line

hello_world("PYTHON 20202")