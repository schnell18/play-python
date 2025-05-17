#!/usr/bin/env python3


class CustomError(Exception):
    pass


def tricky():
    try:
        raise CustomError("First")
    except CustomError:
        try:
            raise CustomError("Second")
        finally:
            print("Finally", end=", ")
        print("End try", end=", ")
    finally:
        print("Finish", end=", ")


if __name__ == "__main__":
    tricky()
