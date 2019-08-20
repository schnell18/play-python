#!/usr/bin/env python3
import time

if __name__ == '__main__':
    num_seconds = 3
    for countdown in reversed(range(num_seconds + 1)):
        if countdown > 0:
            # print to stdout is line-buffered and block-buffered, so this does NOT work
            # print(countdown, end='...')
            # flush=True make the output unbuffered
            print(countdown, end='...', flush=True)
            time.sleep(1)
        else:
            print('Go!')