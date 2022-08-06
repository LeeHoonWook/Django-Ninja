from ninja.router import Router
import time
import asyncio
from app.utils import log_timer, main

ninja = Router()


@ninja.get("/crawling")
@log_timer
def hello(request):
    return "Hello world"


@ninja.get("/say-after")
async def say_after(request, delay: int, word: str):
    await asyncio.sleep(delay)
    return {"saying": word}
