import asyncio
import aiofiles
import aiohttp
import json
from pathlib import Path

async def read_file(input_file):
    async with aiofiles.open(input_file,"r") as f:
        poke_names= (await f.read()).splitlines()
        if poke_names:
            return poke_names
        else:
            return []
        
async def fetch(name,session,url):
    try:
        async with session.get(url) as response:
            response.raise_for_status()
            data= await response.json()
            return {"name":name,"type":(name,data["types"][0]["type"]["name"])}
        
    except Exception as e:
        print(f"failed to get details of {name}\n{e}")
        return

async def save_to_json(data,output_file):
    if data:
        async with aiofiles.open(output_file,"w") as f:
            content= json.dumps(data,indent=2)
            await f.write(content)
            print(f"saved data Successfully into {output_file}")
    else:
        print("There is no valid pokemon details in the urls")
        return
    
async def main():
    file="poke_details.txt"
    out_file="poke_saved.json"

    if Path(file).is_file():
        names= await read_file(file)

        if names:
            urls=[f"https://pokeapi.co/api/v2/pokemon/{name}" for name in names]

            async with aiohttp.ClientSession() as session:
                tasks=[fetch(name,session,url) for name,url in zip(names,urls)]
                results= await asyncio.gather(*tasks)
                result=[r for r in results if r is not None]

            await save_to_json(result,out_file)
        else:
            print(f"{file} is empty")

    else:
        print(f"Invalid file")

asyncio.run(main())