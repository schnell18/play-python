#!/usr/bin/env python3

# Reference: https://docs.python.org/3/library/asyncio-task.html

import asyncio
import time


# async def main():
#     print("Hello")
#     await asyncio.sleep(1)
#     print("world")


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def main1():
    print("*" * 60)
    print("As independent coroutines...")
    print("*" * 60)
    print(f"Started at {time.strftime('%X')}")
    await say_after(1, "Hello")
    await say_after(2, "World")

    print(f"Finished at {time.strftime('%X')}")


async def main2():
    print("*" * 60)
    print("With asyncio.create_task()...")
    print("*" * 60)
    print(f"Started at {time.strftime('%X')}")

    task1 = asyncio.create_task(say_after(1, "Hello"))
    task2 = asyncio.create_task(say_after(2, "World"))
    await task1
    await task2

    print(f"Finished at {time.strftime('%X')}")


async def main3():
    print("*" * 60)
    print("With asyncio.TaskGroup()...")
    print("*" * 60)

    async with asyncio.TaskGroup() as tg:
        tg.create_task(say_after(1, "Hello"))
        tg.create_task(say_after(2, "World"))
        print(f"Started at {time.strftime('%X')}")

    print(f"Finished at {time.strftime('%X')}")

if __name__ == "__main__":
    # To execute a coroutine, we need wrap the call to the top level method
    # inside the asyncio.run() function. And prefix the call to a non-toplevel
    # coroutine method with await.
    asyncio.run(main1())
    asyncio.run(main2())
    asyncio.run(main3())
