#!/usr/bin/env python

def main():
    name = input("What's your name? ")
    print(hello(name))
    # print("Hello,", name)
    # print("Hello,", sep=" ", end="")
    # print(name)
    name = input("What's your name? ").strip().title()
    # print(f"Hello, {name}")
    print(hello(name))


def hello(name="world"):
    return f"Hello, {name}"


"""
Simple hello world program
"""
if __name__ == "__main__":
    main()
