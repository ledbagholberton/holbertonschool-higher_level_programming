#!/usr/bin/python3
def append_write(filename="", text=""):
    with open(filename, 'a', encoding='utf-8') as f:
        ch = f.write(text)
        return ch
