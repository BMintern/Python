import asyncio

async def main():
    print('vaibhavi')
    task= asyncio.create_task(AP('text'))
    print('finished')

async def AP(text):
    print(text)
    await asyncio.sleep(1)

asyncio.run(main())