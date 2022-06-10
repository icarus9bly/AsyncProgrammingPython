import asyncio

async def main():
    print("Aditya")
    task = asyncio.create_task(noman())
    # await noman() # how to await function
    # await task
    await asyncio.sleep(2)
    print("Singh")
    
async def noman():
    print("Pratap")
    await asyncio.sleep(3)

asyncio.run(main())