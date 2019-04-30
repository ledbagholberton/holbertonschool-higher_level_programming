#!/usr/bin/python3


def remove_char_at(str, n):
    result = []
    leng = len(str) + 1
    for i in range(0, leng):
        a = str[i]
        if (i != n):
#            print("{}".format(str[i]), end='')
            result.append(a)
    return result
