import asyncio
import random

async def test(x):
    await asyncio.sleep(x)
    print("done in under 3 seconds")

async def main():
    x= random.randint(1,5)
    try:
        await asyncio.wait_for(test(x), timeout=3)  
    except asyncio.TimeoutError:
        print("timmeouterror")

asyncio.run(main())