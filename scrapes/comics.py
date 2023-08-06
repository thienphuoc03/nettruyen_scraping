import os
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from database.data_handler import save_comic
from scrapes.comics_categories import comic_category_scrape
from utils.utils import print_congratulation


def comic_scrape(url):
    try:
        req = Request(url, headers={"User-Agent": "XYZ/3.0"})
        res = urlopen(req).read()

        if res:
            soup = BeautifulSoup(res, "html.parser")
            total_page = (
                soup.find("ul", class_="pagination")
                .find("li", class_="hidden")
                .text.split(" / ")[1]
                .strip()
            )

            comics_page = []
            for page in range(1, int(total_page) + 1):
                print("Scraping comics page: ", page, "/", total_page)

                list_comic = comic_page_scrape(url + f"?page={page}")
                for comic in list_comic:
                    comics_page.append(comic)

                # clear terminal
                os.system("cls" if os.name == "nt" else "clear")

                print("Scraped comics page: ", page, "/", total_page)

            print_congratulation()
            return comics_page
    except Exception as e:
        print("Error scraping comic:", e)


def comic_page_scrape(url):
    try:
        req = Request(url, headers={"User-Agent": "XYZ/3.0"})
        res = urlopen(req).read()

        if res:
            soup = BeautifulSoup(res, "html.parser")

            comics = []
            list_category = []
            for comic in soup.find_all("div", class_="item"):
                url = comic.find("h3").find("a").get("href")

                comic_detail, list_category = comic_detail_scrape(url)

                comics.extend((comic_detail))

            # save list comic to database
            save_comic(comics)

            with_comic_category_scrape(comics, list_category)

            return comics
    except Exception as e:
        print("Error scraping comic in page:", e)


def with_comic_category_scrape(comics, list_category):
    try:
        for comic in comics:
            comic_category_scrape(comic[0], list_category)
    except Exception as e:
        print("Error scraping comic categories:", e)


def comic_detail_scrape(url):
    try:
        req = Request(url, headers={"User-Agent": "XYZ/3.0"})
        res = urlopen(req).read()

        if res:
            soup = BeautifulSoup(res, "html.parser")
            container = soup.find("article", id="item-detail")

            comic = []
            name = container.find("h1", class_="title-detail").text.strip()
            thumbnail = container.find("img").get("src")
            url = url
            content = (
                container.find("div", class_="detail-content").find("p").text.strip()
            )
            author = (
                container.find("li", class_="author row")
                .find("p", class_="col-xs-8")
                .text.strip()
            )
            status = (
                container.find("li", class_="status row")
                .find("p", class_="col-xs-8")
                .text.strip()
            )
            view = container.find("span", itemprop="ratingCount").text.strip()
            rating = container.find("span", itemprop="ratingValue").text.strip()
            followers = container.find("div", class_="follow").find("b").text.strip()

            # get categories
            list_category = []
            for category in container.find("li", class_="kind row").find_all("a"):
                category = category.text.strip()

                list_category.append(category)

            comic.append(
                (name, thumbnail, url, content, author, status, view, rating, followers)
            )

            print("Scraped comic: ", name)

            return comic, list_category
    except Exception as e:
        print("Error scraping comic detail:", e)
