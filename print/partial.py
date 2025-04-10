#!/usr/bin/env python3
import sys
from functools import partial

if __name__ == "__main__":
    redirect = lambda function, stream: partial(function, file=stream)
    prefix = lambda function, prefix: partial(function, prefix)
    error = prefix(redirect(print, sys.stderr), "[ERROR]")
    error("hello world")
