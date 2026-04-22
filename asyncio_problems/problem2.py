import asyncio
import time

async def task_1():
    print("task_1")
    await asyncio.sleep(1)

async def task_2():
    print("task_2")
    await asyncio.sleep(1)

async def task_3():
    print("task_3")
    await asyncio.sleep(1)

async def main():
    start= time.time()
    await task_1()
    await task_2()
    await task_3()
    end= time.time()
    print(f"total time taken = {end-start}")

asyncio.run(main())