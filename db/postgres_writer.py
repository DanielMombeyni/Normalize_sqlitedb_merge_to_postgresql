import psycopg2
from config import DB_CONFIG


def insert_ads(ads):
    conn = psycopg2.connect(**DB_CONFIG["postgres"])
    cursor = conn.cursor()

    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS ads (
        id INTEGER PRIMARY KEY,
        title VARCHAR NOT NULL,
        game VARCHAR NOT NULL,
        price DECIMAL(10,2),
        location VARCHAR,
        url VARCHAR NOT NULL UNIQUE
    );
    """
    )

    for ad in ads:
        cursor.execute(
            """
        INSERT INTO ads (id, title, game, price, location, url)
        VALUES (%s, %s, %s, %s, %s, %s)
        ON CONFLICT (id) DO NOTHING;
        """,
            (ad["id"], ad["title"], ad["game"], ad["price"], ad["location"], ad["url"]),
        )

    conn.commit()
    cursor.close()
    conn.close()
