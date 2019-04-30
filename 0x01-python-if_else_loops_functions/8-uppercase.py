#!/usr/bin/python3


def uppercase(str):
    result = []
    for i in range(0, len(str)):
        a = ord(str[i])
        if (a > 96 and a < 123):
            a = a - 32
        print("{}".format(chr(a)), end="")
    print()
