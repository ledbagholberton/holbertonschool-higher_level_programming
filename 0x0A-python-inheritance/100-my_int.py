#!/usr/bin/python3
class MyInt(int):
    def __eq__(self, mi_int):
            return int(self) != mi_int

    def __ne__(self, mi_int):
            return int(self) == mi_int
