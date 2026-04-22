import asyncio
import aiohttp

async def fetch_poke(session,url):
    async with session.get(url) as response:
        return await response.json()
    
async def main():
    urls=[f"https://pokeapi.co/api/v2/pokemon/{i}" for i in range(1,11)]
    
    async with aiohttp.ClientSession() as session:
        tasks=[fetch_poke(session,url) for url in urls]
        results= await asyncio.gather(*tasks)

        for pokemon in results:
            print(pokemon["name"])

asyncio.run(main())