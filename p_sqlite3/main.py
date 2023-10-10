# DOCS SQLite: https://www.sqlite.org/doclist.html

import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'

# Open connection with my DB
connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, weight REAL)'
)

connection.commit()

# Close my connection with DB
cursor.close()
connection.close()
