import asyncio
import aiohttp

async def fetch_poke(session,url):
    try:
        async with session.get(url) as response:
            response.raise_for_status()
            data= await response.json()
            return (url,data)
        
    except Exception as e:
        return (url,e)
    
async def main():
    urls=["https://pokeapi.co/api/v2/pokemon/1",
          "https://pokeapi.co/api/v2/pokemon/2",
          "https://pokeapi.co/api/v2/pokemon/sdc",
          "https://pokeapi.co/api/v2/pokemon/4"]
    
    async with aiohttp.ClientSession() as session:
        tasks=[fetch_poke(session,url) for url in urls]
        results= await asyncio.gather(*tasks)

        for url,pokemon in results:
            if isinstance(pokemon,Exception):
                print(f"{url} failed: {pokemon}")
            else:
                print(f"{url} sucsess: {pokemon['name']}")

asyncio.run(main())