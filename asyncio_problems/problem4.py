import asyncio
import time

async def fetch_data(name,delay):
    await asyncio.sleep(delay)
    return f"data from {name}"

async def main():
    start= time.time()
    names= [("shbham",1),("sahil",3),("anubhav",4),("siddhu",2),("vashu",5)]
    tasks= [fetch_data(i,j) for i,j in names]
    results = await asyncio.gather(*tasks)
    for result in results:
        print(result)
    end=time.time()
    print(f"total time = {end-start}")

asyncio.run(main())