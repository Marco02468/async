import asyncio
import time


async def evenMoreAwesomeCalculation():
    await asyncio.sleep(2)  # imagine sophisticated calculations here
    return 'four (I am a coroutine)'


async def awesomeStuff():
    await asyncio.sleep(2)  # imagine sophisticated calculations here
    print('three (I am a coroutine)')


async def someSlowAndUnreliableStuff():
    await asyncio.sleep(2)  # imagine sophisticated calculations here.
    return 'two (I am a coroutine)'


async def main():
    t = time.time()
    print(f"starting")

    # some slow stuff that is needed immediately before we can continue
    # 'await' is for halting the program. Useful for receiving messages for example
    print('one')
    result = await someSlowAndUnreliableStuff()
    print(result)

    # regular coroutine without return value
    # create_task is the important keyword here and make the code truly asynchronous
    # useful for writing a database for example
    awesomeTask1 = asyncio.create_task(awesomeStuff())  # returns three
    await asyncio.sleep(1)
    await awesomeTask1  # roadblock for synchronising everything again

    # when we wait for a value we need later but can prepare some stuff in the meanwhile
    awesomeTask2 = asyncio.create_task(evenMoreAwesomeCalculation())  # returns five
    await asyncio.sleep(1)
    print('five')
    result = await awesomeTask2
    print(result)

    t2 = time.time()-t
    print(f"execution time {t2}")
    # we sleep for a total of 8 seconds but execution time was only a bit more than 6 seconds


if __name__ == "__main__":
    asyncio.run(main())
