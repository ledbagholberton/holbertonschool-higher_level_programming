#!/usr/bin/python3
def multiple_returns(sentence):
    long = len(sentence)
    if long == 0:
        chr = None
    else:
        chr = sentence[0]
    tupla = long, chr
    return tupla
