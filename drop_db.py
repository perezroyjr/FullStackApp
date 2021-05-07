import sqlite3
from config import *

connection = sqlite3.connect(DB_FILE)

cursor = connection.cursor()

cursor.execute("""
    DROP TABLE stock_price
""")

cursor.execute("""
    DROP TABLE stock
""")

connection.commit()