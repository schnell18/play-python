#!/usr/bin/env python3
from collections import namedtuple

if __name__ == '__main__':
    Person = namedtuple('Person', 'name age')
    jdoe = Person('John Doe', 42)
    print(jdoe)