import asyncio

async def lion(name):
    print(f"My name is {name}. I'm a lion")
    return name

async def dog(name):
    print(f"My name is {name}. I'm a dog")
    await asyncio.sleep(2)
    print("Bark")

async def main():
    print('Monumental stuff')
    # await lion("Balba")
    task1 = asyncio.create_task(lion("Balba"))
    task2 = asyncio.create_task(dog("Salba"))
    # Tasks when awaited returns future
    value = await task1
    print(value)
    await task2
    


asyncio.run(main())