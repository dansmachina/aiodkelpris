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



```

## Data sources

[Energi Data Service](https://www.energidataservice.dk/tso-electricity/Elspotprices).
