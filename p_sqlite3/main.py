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

# THE FAMOUS DELETE SEM WHERE
cursor.execute(f'DELETE FROM {TABLE_NAME}')

cursor.execute(f'DELETE FROM sqlite_sequence WHERE name ="{TABLE_NAME}"')
# Create table
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, weight REAL)'
)
# Exec create table
connection.commit()

# Register a value in the columm
# WARNING: cuidado com sql injection
cursor.execute(
    f'INSERT INTO {TABLE_NAME} (id, name, weight) VALUES (NULL, "Caio Dantas", 105.6), (NULL, "UISH Kiasn", 123.6), (NULL, "Esdu Iekm", 105.6), (NULL, "Grigo Hur", 102), (NULL, "Isadora Dantas", 78.9)')

connection.commit()

# Close my connection with DB
cursor.close()
connection.close()
