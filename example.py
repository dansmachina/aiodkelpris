import asyncio

import aiohttp

from aioelpris import DKElPris
from aioelpris.core.models import Price


async def example():
    async with aiohttp.ClientSession() as session:
        pris = DKElPris(session=session, price_area="SE3")
        price: Price = await pris.get_current_price()
        print(price)
        return price


asyncio.run(example())
