#!/usr/bin/env python3

if __name__ == "__main__":
    with open("no-newline.py") as f:
        for line in f:
            print(line)
            # print(line, end='')

