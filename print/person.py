#!/usr/bin/env python3
from dataclasses import dataclass


@dataclass
class Person:
    name: str
    age: int

    def celebrate_birthday(self):
        self.age += 1


if __name__ == "__main__":
    jdoe = Person("John Doe", 42)
    print(jdoe)
    jdoe.celebrate_birthday()
    print(jdoe)

