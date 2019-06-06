#!/usr/bin/python3
def pascal_triangle(n):
    if n <= 0:
        my_list = []
        return my_list
    my_list = [1]
    for i in range(n):
        for j in range(n):
            my_list[
