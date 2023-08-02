from urllib.request import Request, urlopen
from bs4 import BeautifulSoup


def comic_scrape(url):
    try:
        req = Request(url, headers={"User-Agent": "XYZ/3.0"})
        res = urlopen(req).read()

        if res:
            soup = BeautifulSoup(res, "html.parser")
            # total_page = (
            #     soup.find("ul", class_="pagination")
            #     .find("li", class_="hidden")
            #     .text.split(" / ")[1]
            #     .strip()
            # )

            total_page = 1

            comics_page = []
            for page in range(1, int(total_page) + 1):
                print("Scraping comics page: ", page)
                list_comic = comic_page_scrape(url + f"?page={page}")
                for comic in list_comic:
                    comics_page.append(comic)

            print("*** *** *** Congratulation *** *** ***")
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
            for comic in soup.find_all("div", class_="item"):
                url = comic.find("h3").find("a").get("href")

                comic_detail = comic_detail_scrape(url)
                comics.append((comic_detail))

            print("Scraped comics")
            return comics
    except Exception as e:
        print("Error scraping comic in page:", e)


def comic_detail_scrape(url):
    try:
        req = Request(url, headers={"User-Agent": "XYZ/3.0"})
        res = urlopen(req).read()

        if res:
            soup = BeautifulSoup(res, "html.parser")
            container = soup.find("article", id="item-detail")

            comic = {}
            comic["name"] = container.find("h1", class_="title-detail").text.strip()
            comic["url"] = url
            comic["thumbnail"] = container.find("img").get("src")
            comic["author"] = (
                container.find("li", class_="author row")
                .find("p", class_="col-xs-8")
                .text.strip()
            )
            comic["status"] = (
                container.find("li", class_="status row")
                .find("p", class_="col-xs-8")
                .text.strip()
            )
            comic["view"] = container.find("span", itemprop="ratingCount").text.strip()
            comic["rating"] = container.find(
                "span", itemprop="ratingValue"
            ).text.strip()
            comic["content"] = (
                container.find("div", class_="detail-content").find("p").text.strip()
            )

            list_chapters = []
            chapter_info = {}
            list_chapters_container = container.find("div", id="nt_listchapter")
            for chapter in list_chapters_container.find_all("li", class_="row"):
                chapter_info["name"] = (
                    chapter.find("div", class_="col-xs-5 chapter")
                    .find("a")
                    .text.strip()
                )
                chapter_info["url"] = (
                    chapter.find("div", class_="col-xs-5 chapter").find("a").get("href")
                )
                chapter_info["update_at"] = chapter.find(
                    "div", class_="col-xs-4 text-center no-wrap small"
                ).text.strip()
                chapter_info["view"] = chapter.find(
                    "div", class_="col-xs-3 text-center small"
                ).text.strip()

                comic_images_chapter_scrape(chapter_info["url"])

                list_chapters.insert(0, chapter_info)

            comic["chapters"] = list_chapters

            print("Scraped comic: ", comic["name"])
            return comic
    except Exception as e:
        print("Error scraping comic detail:", e)


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
