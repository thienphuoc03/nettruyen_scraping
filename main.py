import os
from os.path import join, dirname
from dotenv import load_dotenv
from scrapes.categories import category_scrape

from scrapes.comics import comic_scrape
from database.data_handler import save_category

dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)


# URL of the website to scrape
url = os.environ.get("WEBSITE_URL") or "https://www.nettruyenio.com/"

# Scrape the website
# categories
categories = category_scrape(url + "tim-truyen")
if categories:
    save_category(categories)

# comics
if categories:
    comics = comic_scrape(url + "tim-truyen")
comics = comic_scrape(url + "tim-truyen")
