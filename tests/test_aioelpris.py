import json
import unittest
from datetime import datetime, timedelta

from aiohttp import ClientSession
from aiohttp.test_utils import AioHTTPTestCase

from aioelpris.pris import BASE_URL, DATE_TIME_FORMAT, PRICE_AREA, ElPris, Price


class TestElPris(AioHTTPTestCase):
    async def get_application(self):
        return None

    async def setUpAsync(self):
        self.session = ClientSession()

    async def tearDownAsync(self):
        await self.session.close()

    async def test_invalid_price_area(self):
        with self.assertRaises(ValueError):
            ElPris(session=self.session, price_area="INVALID_AREA")

    async def test_valid_price_area(self):
        el_pris = ElPris(session=self.session, price_area=PRICE_AREA[0])
        self.assertEqual(el_pris.price_area, PRICE_AREA[0])

    async def test_api_get_prices(self):
        el_pris = ElPris(session=self.session, price_area=PRICE_AREA[0])
        now = datetime.now()
        now_plus_one = now + timedelta(hours=1)
        start = datetime.strftime(now, DATE_TIME_FORMAT)
        end = datetime.strftime(now_plus_one, DATE_TIME_FORMAT)
        _filter = {"PriceArea": el_pris.price_area}
        url = BASE_URL.format(filter=json.dumps(_filter), start=start, end=end, limit=1)
        prices = await el_pris._api_get_prices(url)
        self.assertIsInstance(prices, list)
        self.assertIsInstance(prices[0], dict)

    async def test_retrieve_prices(self):
        el_pris = ElPris(session=self.session, price_area=PRICE_AREA[0])
        now = datetime.now()
        now_plus_one = now + timedelta(hours=1)
        start = datetime.strftime(now, DATE_TIME_FORMAT)
        end = datetime.strftime(now_plus_one, DATE_TIME_FORMAT)
        prices = await el_pris._retrieve_prices(start, end, 1)
        self.assertIsInstance(prices, list)
        self.assertIsInstance(prices[0], dict)

    async def test_get_current_price(self):
        el_pris = ElPris(session=self.session, price_area=PRICE_AREA[0])
        current_price = await el_pris.get_current_price()
        self.assertIsInstance(current_price, Price)


if __name__ == "__main__":
    unittest.main()
