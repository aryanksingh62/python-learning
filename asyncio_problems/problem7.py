import asyncio
import aiofiles
from pathlib import Path

async def read_content(input_file):
        async with aiofiles.open(input_file,"r") as f:
            content= await f.read()
            if content:
                return content.upper()
            else:
                 print(f"{input_file} is empty")
                 return
            
async def write_content(output_file,data):
    async with aiofiles.open(output_file,"w") as f:
        await f.write(data)
        print("output written succcesfully")

async def main():
    INPUTFILE= "1.txt"
    OUTPUTFILE= "out.txt"

    if not  Path(INPUTFILE).is_file():
        print(f"{INPUTFILE}: file not found")
    else:
        content = await read_content(INPUTFILE)
        if content:
            await write_content(OUTPUTFILE,content)

asyncio.run(main())