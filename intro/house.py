#!/usr/bin/env python

def main():
    name = input("What's your name? ")

    # if name == 'Harry':
    #     print("Gryffindor")
    # elif name == 'Hermione':
    #     print("Gryffindor")
    # elif name == 'Ron':
    #     print("Gryffindor")
    # elif name == 'Draco':
    #     print("Slytherin")
    # else:
    #     print("Who?")

    # if name == 'Harry' or name == 'Hermione' or name == 'Ron':
    #     print("Gryffindor")
    # elif name == 'Draco':
    #     print("Slytherin")
    # else:
    #     print("Who?")

    match name:
        case "Harry" | "Hermione" | "Ron":
            print("Gryffindor")
        case "Draco":
            print("Slytherin")
        case _:
            print("Who?")

if __name__ == "__main__":
    main()

