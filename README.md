# aioelpris

An aio library to retrieve current electricity price in (some parts) of the Nordics. Current supported regions are:

- `DK1`: Denmark/west of the Great Belt
- `DK2`: Denmark/east of the Great Belt
- `NO2`: Norway/Kristiansand
- `SE3`: Sweden/Stockholm
- `SE4`: Sweden/Malmö

Prices are returned in DKK and EUR currencies.

## Basic example

```python

import asyncio

import aiohttp

from aiodkelpris import DKElPris
from aiodkelpris.core.models import Price

async def example():
    async with aiohttp.ClientSession() as session:
        pris = DKElPris(session=session, price_area="DK1")
        price: Price = await pris.get_current_price()
        print(price)
        return price

asyncio.run(example())

```

## Data sources

[Energi Data Service](https://www.energidataservice.dk/tso-electricity/Elspotprices).
