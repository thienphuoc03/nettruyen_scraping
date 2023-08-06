from connection import get_connection


def create_tables():
    try:
        conn = get_connection()
        if conn:
            cursor = conn.cursor()

            # Create categories table
            create_categories_table_query = """
            CREATE TABLE IF NOT EXISTS categories (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255),
                url LONGTEXT,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
            )
            """
            cursor.execute(create_categories_table_query)

            # Create comics table
            create_comics_table_query = """
            CREATE TABLE IF NOT EXISTS comics (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255),
                thumbnail VARCHAR(255),
                url VARCHAR(255),
                content LONGTEXT,
                author VARCHAR(255),
                status VARCHAR(255),
                view INT,
                rating FLOAT,
                followers INT,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
            )
            """
            cursor.execute(create_comics_table_query)

            # Create comics_categories table
            create_comics_categories_table_query = """
            CREATE TABLE IF NOT EXISTS comics_categories (
                comic_id INT,
                category_id INT,
                PRIMARY KEY (comic_id, category_id),
                FOREIGN KEY (comic_id) REFERENCES comics(id) ON DELETE CASCADE,
                FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE CASCADE
            )
            """
            cursor.execute(create_comics_categories_table_query)

            # Create chapters table
            create_chapters_table_query = """
            CREATE TABLE IF NOT EXISTS chapters (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255),
                url VARCHAR(255),
                view INT,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                comic_id INT,
                FOREIGN KEY (comic_id) REFERENCES comics(id) ON DELETE CASCADE
            )
            """
            cursor.execute(create_chapters_table_query)

            # Create chapter_images table
            create_chapter_images_table_query = """
            CREATE TABLE IF NOT EXISTS chapter_images (
                id INT AUTO_INCREMENT PRIMARY KEY,
                url VARCHAR(255),
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                chapter_id INT,
                FOREIGN KEY (chapter_id) REFERENCES chapters(id) ON DELETE CASCADE
            )
            """
            cursor.execute(create_chapter_images_table_query)

            # Commit changes and close connection
            conn.commit()
            cursor.close()
            conn.close()

            print("Tables successfully created.")

            return
    except Exception as e:
        print("Error create table:", e)


if __name__ == "__main__":
    create_tables()
