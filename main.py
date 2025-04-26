from loguru import logger
import os
from datetime import date
import xml.etree.ElementTree as ET
import pandas as pd
from icecream import ic
import requests
from bs4 import BeautifulSoup


def main():
    url = "https://en.m.wikipedia.org/wiki/List_of_Justice_League_members"
    html_file = "data/justice_league_members.html"
    if not os.path.exists(html_file):
        logger.info("Downloading HTML file...")
        response = requests.get(url)
        with open(html_file, "wb") as file:
            file.write(response.content)

    with open(html_file, "r", encoding="utf-8") as file:
        dfs = pd.read_html(file)

    for i, table in enumerate(dfs):
        logger.info(f"Table {i}: {table.shape}")
        if i == 0:
            logger.info("Skipping first table")
            continue

        if table.shape[0] > 0:
            logger.info(table.head())
            table.to_csv(f"data/justice_league_members_{i}.csv", index=False)
    # df = pd.concat(dfs, ignore_index=True)


    # ic(df)


    return


if __name__ == "__main__":
    os.makedirs("logs", exist_ok=True)
    os.makedirs("data", exist_ok=True)
    logger.add(f"logs/{date.today().strftime('%Y-%m-%d')}.log", rotation="1 day", retention="10 days", compression="zip")

    main()



