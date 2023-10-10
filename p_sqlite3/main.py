import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME

# Open connection with my DB
connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# Close my connection with DB
cursor.close()
connection.close()
