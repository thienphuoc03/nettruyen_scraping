from database.connection import get_connection


def save_category(categories):
    try:
        conn = get_connection()
        if conn:
            print("Inserting data of CATEGORY to MySQL...")
            cursor = conn.cursor()

            # Insert data into the table
            insert_query = "INSERT INTO categories (name, url) VALUES (%s, %s)"
            cursor.executemany(insert_query, categories)

            # Commit changes and close connection
            conn.commit()

        cursor.close()
        conn.close()
        print("*.*Successfully*.*")

        return
    except Exception as e:
        print("Error insert category: ", e)


def save_comic(comics):
    try:
        conn = get_connection()
        if conn:
            print("Inserting data of COMIC to MySQL...")
            cursor = conn.cursor()

            # Insert data into the table
            insert_query = "INSERT INTO comics (name, thumbnail, url, content, author, status, view, rating, followers) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.executemany(insert_query, comics)

            # Commit changes and close connection
            conn.commit()

        cursor.close()
        conn.close()
        print("*.*Successfully*.*")

        return
    except Exception as e:
        print("Error:", e)


def save_comics_categories(comic_id, list_category_id):
    try:
        conn = get_connection()

        if conn:
            # print("Insert data comics_categories")
            cursor = conn.cursor()

            for category_id in list_category_id:
                insert_query = "INSERT INTO comics_categories (comic_id, category_id) VALUES (%s, %s)"
                values = (comic_id, category_id)

                cursor.execute(insert_query, values)

                conn.commit()

        cursor.close()
        conn.close()
        # print("*.*Successfully*.*")

        return
    except Exception as e:
        print("Error insert comics_categories: ", e)
