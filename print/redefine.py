#!/usr/bin/env python3
import builtins

println = builtins.print


def print(*args, **kwargs):
    builtins.print(*args, **kwargs, end="")


if __name__ == "__main__":
    print("hello world")
    println("hello world")

