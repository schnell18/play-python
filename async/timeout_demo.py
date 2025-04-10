#!/usr/bin/env python3

import asyncio


async def long_running_task(duration=4):
    await asyncio.sleep(duration)


async def main(duration=4):
    try:
        async with asyncio.timeout(5):
            await long_running_task(duration)
    except TimeoutError:
        print("Task runs out of time!")
        return

    print("Task completed!!!")


if __name__ == "__main__":
    print("*" * 60)
    print("No timeout demo...")
    print("*" * 60)
    asyncio.run(main(3))

    print("*" * 60)
    print("Timeout demo...")
    print("*" * 60)
    asyncio.run(main(6))
