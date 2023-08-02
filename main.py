import os
from dotenv import load_dotenv
from scrapes.categories import category_scrape
from scrapes.comics import comic_scrape
from database.data_handler import save_category
from database.create_tables import create_tables

load_dotenv()


# URL of the website to scrape
url = os.getenv("WEBSITE_URL") or "https://www.nettruyenio.com/"

# create_tables()

# Scrape the website
# categories
# categories = category_scrape(url + "tim-truyen")
# if categories:
#     save_category(categories)

# # comics
# if categories:
#     for category in categories:
#         comics = comic_scrape(url + "tim-truyen")
comics = comic_scrape(url + "tim-truyen")

print(comics)
