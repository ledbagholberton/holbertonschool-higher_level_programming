#!/usr/bin/python3
def read_file(filename=""):
    with open(filename, 'r', encoding = 'utf-8') as f:
        a = f.read()
        print("{:s}".format(a))
