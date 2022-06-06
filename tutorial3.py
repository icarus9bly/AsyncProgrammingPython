import asyncio

def normal_function():
    return "something"

async def fetch_data():
    print ('Start fetching....')
    await asyncio.sleep(2) # Waiting for 2 seconds, meanwhile print_numbers can be run
    print ('Done fetching....')
    return {'data' : 1}

async def print_numbers():
    for i in range(10) :
        print(i)
        await asyncio.sleep (0.25)    
async def main() :
    task1 = asyncio.create_task(fetch_data()) # Task 1 created
    task2 = asyncio.create_task(print_numbers())
    value = await task1 # Waiting for task 1 to complete
    print(value)
    await task2 # If we don't wait for task2, as soon as task1 completes our execution will complete
    # value2 = await asyncio.get_event_loop().run_in_executor(None, normal_function)
    value2 = await fetch_data()
    print(value2)
asyncio.run(main()) # Creates a event loop
