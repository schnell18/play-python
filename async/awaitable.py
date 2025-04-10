#!/usr/bin/env python3

# Reference: https://docs.python.org/3/library/asyncio-task.html

import asyncio


async def nested():
    return 42


async def main1():
    print("*" * 60)
    print("Call async function w/o await...")
    print("*" * 60)

    nested()
    print(f"result={await nested()}")


async def main2():
    print("*" * 60)
    print("Call async function w/ create_task()...")
    print("*" * 60)

    task = asyncio.create_task(nested())
    print(f"result={await task}")


# async def main():
#     await function_that_returns_a_future_object()
#
#     # this is also valid:
#     await asyncio.gather(
#         function_that_returns_a_future_object(),
#         some_python_coroutine()
#     )

if __name__ == "__main__":
    # To execute a coroutine, we need wrap the call to the top level method
    # inside the asyncio.run() function. And prefix the call to a non-toplevel
    # coroutine method with await.
    asyncio.run(main1())
    asyncio.run(main2())
