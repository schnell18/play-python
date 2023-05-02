#!/usr/bin/env python

def main():
    print_square(10)
    print_column(3)
    print_row(5)

def print_column(n):
    for _ in range(n):
        print("#")

def print_row(n):
    print("#" * n)

def print_square(n):
    for _ in range(n):
        print("#" * n)

if __name__ == "__main__":
    main()




