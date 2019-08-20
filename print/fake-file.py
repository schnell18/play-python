#!/usr/bin/env python3
import io

if __name__ == '__main__':
    fake_file = io.StringIO()
    print('hello world', file=fake_file)
    print(fake_file.getvalue())