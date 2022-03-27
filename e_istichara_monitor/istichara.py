import logging
import sqlite3
import sys
from time import time_ns

import pandas as pd
import requests
import schedule
import tenacity
from loguru import logger as llogger
from tenacity import retry

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
logger = logging.getLogger(__name__)

session = requests.Session()
headers = {"Accept-Language": "ar"}

urls = {
    "home": "https://www.e-istichara.tn/home",
    "by_gov": "https://www.e-istichara.tn/istichara/statistique-by-gouv",
    "by_gender": "https://www.e-istichara.tn/istichara/statistique-by-genre",
    "by_theme": "https://www.e-istichara.tn/istichara/statistique-by-module",
    "by_country": "https://www.e-istichara.tn/istichara/statistique-by-pays",
    "by_age": "https://www.e-istichara.tn/istichara/statistique-by-age",
}

session.get(urls["home"])

con = sqlite3.connect("istichara.sqlite")


@retry(
    wait=tenacity.wait.wait_random(
        60, 120
    ),  # When retrying, wait between one minute and two minutes
    stop=tenacity.stop.stop_after_attempt(5),  # Give up on retrying after five attempts
    after=tenacity.after.after_log(
        logger=logger, log_level=logging.WARNING
    ),  # Log retry attempts
)
def process_endpoint(endpoint_key: str) -> pd.DataFrame:
    """
    Request the JSON response based the `endpoint_key` then return it as a
    Pandas DataFrame with a timestamp.
    """
    url = urls[endpoint_key]
    response = session.get(url, headers=headers)
    assert response.json() != []
    timestamp = time_ns()
    return pd.DataFrame(response.json()).assign(timestamp=timestamp)


def main():
    """
    Iterate through endpoints to request their data,
    which are saved to a local SQLite3 Database.
    """
    llogger.info("Running")
    for key in urls:
        if "by" in key:
            df = process_endpoint(key)  # Will retry on failure
            df.to_sql(name=key, con=con, if_exists="append", index=False)
    llogger.info("Done")


schedule.every(15).minutes.do(main)  # Request data from all endpoints every 15 minutes

if __name__ == "__main__":
    while True:
        schedule.run_pending()
