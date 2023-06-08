#!/usr/bin/env python3

import argparse

# def meow(n: int) -> None:
#     for _ in range(n):
#         print("meow")


def meow(n: int) -> str:
    """
    Meow n times.

    :param n: Number of times to meow
    :type n: int
    :raise TypeError: If n is not an int
    :return: A string of n meows, one per line
    :rtype: str
    """

    return "meow\n" * n


class Cat:
    MEOWS = 3

    def meow(self):
        for _ in range(Cat.MEOWS):
            print("meow")


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Meow like a kitten")
    parser.add_argument("-n", default=1, help="number of times to meow", type=int)
    args = parser.parse_args()

    # cat = Cat()
    # cat.meow()
    # meows = input("Input times to meow: ")
    # meow(int(meows))
    # print(meow(meows))
    # print(meow(int(meows)))
    for _ in range(args.n):
        print("meow")
