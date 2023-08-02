from urllib.request import Request, urlopen
from bs4 import BeautifulSoup


def category_scrape(url):
    try:
        req = Request(url, headers={"User-Agent": "XYZ/3.0"})
        res = urlopen(req).read()

        if res:
            soup = BeautifulSoup(res, "html.parser")

            container = soup.find("div", class_="Module-179")
            categories = []
            for category in container.find_all("li", class_=False):
                name = category.find("a").text.strip()
                url = category.find("a").get("href")
                categories.append((name, url))

            return categories
    except Exception as e:
        print("Error scraping category:", e)
