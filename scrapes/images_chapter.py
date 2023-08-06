from urllib.request import Request, urlopen
from bs4 import BeautifulSoup


def comic_images_chapter_scrape(url):
    try:
        req = Request(url, headers={"User-Agent": "XYZ/3.0"})
        res = urlopen(req).read()

        if res:
            soup = BeautifulSoup(res, "html.parser")
            images = soup.find_all("div", class_="page-chapter")
            image = {}
            for image in images:
                image["url"] = image.find("img").get("src")

            print("Scraped comic images of chapter: ")
            return image
    except Exception as e:
        print("Error scraping comic images:", e)
