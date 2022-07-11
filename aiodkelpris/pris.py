import asyncio
import json
import logging
from datetime import datetime, timedelta
from typing import List

import aiohttp

from aiodkelpris.core.const import BASE_URL, DATE_TIME_FORMAT, PRICE_AREA
from aiodkelpris.core.models import Price

_LOGGER = logging.getLogger(__name__)


class DKElPris:
    def __init__(
        self,
        *,
        session: aiohttp.ClientSession,
        price_area: str = PRICE_AREA[0],
    ):
        self._session = session
        self.price_area = price_area

        if price_area not in PRICE_AREA:
            _LOGGER.error(
                "Unknown price area %s. Should be one of %s", price_area, PRICE_AREA
            )
            raise ValueError(
                f"Invalid price area: {price_area}. Should be one of {PRICE_AREA}"
            )

    async def _api_get_prices(self, url: str) -> List[Price]:
        assert self._session is not None
        _LOGGER.debug("Requesting: '%s'", url)
        resp = await self._session.get(url)
        if resp.status < 400:
            data = await resp.json()
            return data["records"]
        else:
            _LOGGER.error("Error {}", resp)
            raise Exception(f"Error {resp}")

    async def _retrieve_prices(self, start: str, end: str) -> List[Price]:
        _filter = {"PriceArea": self.price_area}
        url = BASE_URL.format(filter=json.dumps(_filter), start=start, end=end)
        try:
            return await self._api_get_prices(url)
        except asyncio.TimeoutError:
            _LOGGER.warning("Timeout error requesting data from '%s'", url)
            raise Exception(f"Error requesting data from '{url}'")
        except aiohttp.ClientError:
            _LOGGER.warning("Client error in '%s'", url)
            raise Exception(f"Error requesting data from '{url}'")

    async def get_current_price(self) -> Price:
        now = datetime.now()
        now_plus_one = now + timedelta(hours=1)
        start = datetime.strftime(now, DATE_TIME_FORMAT)
        end = datetime.strftime(now_plus_one, DATE_TIME_FORMAT)
        _LOGGER.debug("Time frame requested: %s - %s", start, end)
        price = await self._retrieve_prices(start, end)
        return price[0]
