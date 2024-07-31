#!/usr/bin/env python


def num(a, b, c, *args, **kwargs):
    return b + c + sum(args) + sum(kwargs.values())


print(num(4, 5, 8, 4, i=3, j=2))
