from ninja.router import Router
import time
import asyncio


ninja = Router()


@ninja.get("/hello")
def hello(request):
    return "Hello world"


@ninja.post("/hello")
def hello(request):
    return "Hello world"


@ninja.get("/say-after")
def say_after(request, delay: int, word: str):
    time.sleep(delay)
    return {"saying": word}


@ninja.get("/say-after")
async def say_after(request, delay: int, word: str):
    await asyncio.sleep(delay)
    return {"saying": word}
