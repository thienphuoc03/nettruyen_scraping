from database.connection import get_connection


def save_category(data_list):
    try:
        conn = get_connection()
        if conn:
            print("Inserting data of CATEGORY to MySQL...")
            cursor = conn.cursor()

            # # Drop table if it exists
            # drop_table_query = "DROP TABLE IF EXISTS categories"
            # cursor.execute(drop_table_query)

            # # Create a table if it doesn't exist
            # create_table_query = """
            # CREATE TABLE IF NOT EXISTS categories (
            #     id INT AUTO_INCREMENT PRIMARY KEY,
            #     name VARCHAR(255),
            #     url LONGTEXT,
            #     created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            #     updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
            # )
            # """
            # cursor.execute(create_table_query)

            # Insert data into the table
            insert_query = "INSERT INTO categories (name, url) VALUES (%s, %s)"
            cursor.executemany(insert_query, data_list)

            # Commit changes and close connection
            conn.commit()
            cursor.close()
            conn.close()
            print("*.*Successfully*.*")

            return
    except Exception as e:
        print("Error insert category: ", e)


def save_comic(data_list):
    try:
        print(data_list)
    except Exception as e:
        print("Error:", e)
