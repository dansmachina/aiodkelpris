import asyncio

from aiohttp import ClientSession

from aioelpris import ElPris
from aioelpris.core.models import Price


async def example() -> Price:
    async with ClientSession() as session:
        pris = ElPris(session=session, price_area="SE3")
        price: Price = await pris.get_current_price()
        print(price.SpotPriceDKK)
        return price


asyncio.run(example())
