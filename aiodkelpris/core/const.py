PRICE_AREA = ["DK1", "DK2"]
DATE_TIME_FORMAT = "%Y-%m-%dT%H:00"
DATE_TIME_FORMAT_API = "%Y-%m-%dT%H:00:00"
TZ = "Europe/Copenhagen"
BASE_URL = (
    "https://api.energidataservice.dk/dataset/Elspotprices"
    "?filter={filter}"
    "&start={start}"
    "&end={end}"
    "&limit=1"
)
