#!/usr/bin/env python

def square(n):
    return n * n


if __name__ == "__main__":
    x = int(input("Input x: "))
    y = int(input("Input y: "))

    print("%s + %s = %d" % (x, y, x + y))
    print(f"{x} + {y} = {x+y:,}")
    print(f"{x} / {y} = {x/y:.2f}")

    x = float(input("Input x: "))
    y = float(input("Input y: "))
    print("%f + %f = %f" % (x, y, x + y))
