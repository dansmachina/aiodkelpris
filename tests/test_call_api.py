from datetime import datetime

import pytest
from aiohttp import ClientSession

from aioelpris import DKElPris
from aioelpris.core.const import DATE_TIME_FORMAT, DATE_TIME_FORMAT_API, PRICE_AREA
from aioelpris.core.models import Price


@pytest.mark.asyncio
async def test_call_api():
    async with ClientSession() as session:
        pris = DKElPris(session=session, price_area=PRICE_AREA[0])
        price: Price = await pris.get_current_price()

    now = datetime.now()
    start = datetime.strftime(now, DATE_TIME_FORMAT)
    hour_dk = datetime.strptime(price["HourDK"], DATE_TIME_FORMAT_API)
    hour_dk_formatted = datetime.strftime(hour_dk, DATE_TIME_FORMAT)
    assert price is not None
    assert price["PriceArea"] == "DK1"
    assert hour_dk_formatted == start
    assert isinstance(price["SpotPriceDKK"], float)
