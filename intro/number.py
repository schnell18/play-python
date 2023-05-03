#!/usr/bin/env python

def main():
    n = get_number()
    meow(n)
    x = get_int("What's x? ")
    print(f"x is {x}")

    # try:
    #     x = int(input("What is x? "))
    # except ValueError:
    #     print("x is not an integer")
    # else:
    #     print(f"x is {x}")

    # while True:
    #     try:
    #         x = int(input("What is x? "))
    #     except ValueError:
    #         print("x is not an integer")
    #     else:
    #         break
    # print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass

# def get_int():
#     while True:
#         try:
#             return int(input("What is x? "))
#         except ValueError:
#             pass

def get_number():
    while True:
        try:
            n = int(input("What is n? "))
            if n > 0:
                break
        except ValueError:
            print("n is not an integer")
            pass
    return n

def meow(n):
    for _ in range(n):
        print("meow!")

if __name__ == "__main__":
    main()



