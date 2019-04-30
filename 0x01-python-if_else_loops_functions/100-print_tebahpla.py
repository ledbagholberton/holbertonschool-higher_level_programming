#!/usr/bin/python3
flag = 1
for i in range(122, 96, -1):
    a = i
    if (flag == 1):
        a = i
    else:
        a = i - 32
    flag = flag * -1
    print("{}".format(chr(a)), end="")
