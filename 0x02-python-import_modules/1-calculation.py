#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    c = add(a, b)
    d = sub(a, b)
    e = mul(a, b)
    f = div(a, b)
    print("{:d} + {:d} = {:d}".format(a, b, c))
    print("{:d} - {:d} = {:d}".format(a, b, d))
    print("{:d} * {:d} = {:d}".format(a, b, e))
    print("{:d} / {:d} = {:d}".format(a, b, f))
