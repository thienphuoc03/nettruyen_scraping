from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from database.connection import get_connection
from database.data_handler import save_comics_categories


def comic_category_scrape(comic, list_category):
    try:
        conn = get_connection()
        if conn:
            cursor = conn.cursor()

            # select category id
            categories = []
            for category in list_category:
                category_id_query = """
                    SELECT id FROM categories WHERE name = %s
                """
                category_name = (category,)

                cursor.execute(category_id_query, category_name)

                category_id = cursor.fetchone()

                categories.append(category_id[0])

            # select comic id
            comic_id = """
                SELECT id FROM comics WHERE name = %s
            """
            comic_name = (comic,)

            cursor.execute(comic_id, comic_name)

            comic_id = cursor.fetchone()

            save_comics_categories(comic_id[0], categories)

        cursor.close()
        conn.close()

        return
    except Exception as e:
        print("Error scraping comic category: ", e)
