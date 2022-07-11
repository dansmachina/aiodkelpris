from pydantic import BaseModel


class Price(BaseModel):
    HourUTC: str
    HourDK: str
    PriceArea: str
    SpotPriceDKK: float
    SpotPriceEUR: float

    class Config:
        orm_mode = True
