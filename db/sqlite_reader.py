import sqlite3
import pandas as pd
from config import DB_CONFIG


def get_ads_data():
    conn = sqlite3.connect(DB_CONFIG["sqlite_path"])
    df = pd.read_sql_query("SELECT * FROM ads", conn)
    conn.close()
    return df
