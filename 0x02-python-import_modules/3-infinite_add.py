#!/usr/bin/python3
import sys
suma = 0
for i in range(1, len(sys.argv)):
    suma = suma + int(sys.argv[i])
print("{:d}".format(suma))
