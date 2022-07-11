PRICE_AREA: list[str] = [
    "DK1",  # Denmark/west of the Great Belt
    "DK2",  # Denmark/east of the Great Belt
    "NO2",  # Norway/Kristiansand
    "SE3",  # Sweden/Stockholm
    "SE4",  # Sweden/Malmö
]
DATE_TIME_FORMAT = "%Y-%m-%dT%H:00"
DATE_TIME_FORMAT_API = "%Y-%m-%dT%H:00:00"
BASE_URL = (
    "https://api.energidataservice.dk/dataset/Elspotprices"
    "?filter={filter}"
    "&start={start}"
    "&end={end}"
    "&limit={limit}"
)
