#!/usr/bin/env python3
from functools import partial
import sys

if __name__ == '__main__':
    redirect = lambda function, stream: partial(function, file=stream)
    prefix = lambda function, prefix: partial(function, prefix)
    error = prefix(redirect(print, sys.stderr), '[ERROR]')
    error('hello world')