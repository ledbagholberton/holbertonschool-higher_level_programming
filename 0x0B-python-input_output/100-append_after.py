#!/usr/bin/python3
def append_after(filename="", search_string="", new_string=""):
    with open(filename, 'r') as f:
        pos = 0
        a = f.readline()
        b = ""
        while a:
            if a.count(search_string) > 0:
                b = b + a + new_string
            else:
                b = b + a
            a = f.readline()
    with open(filename, 'w') as f:
        print(b,end="")
        f.write(b)
