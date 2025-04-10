#!/usr/bin/env python

def main():
    x = int(input("What is x? "))

    # if is_even(x):
    #     print("Even")
    # else:
    #     print("Odd")

    print("Even" if is_even(x) else "Odd")

def is_even(x):
    return x % 2 == 0

if __name__ == "__main__":
    main()
