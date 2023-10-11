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

# cursor.execute(f'DELETE FROM sqlite_sequence WHERE name ="{TABLE_NAME}"')
# Create table
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, weight REAL)'
)
# Exec create table
connection.commit()

# Register a value in the columm
# WARNING: cuidado com sql injection
# cursor.execute(
#     f'INSERT INTO {TABLE_NAME} (name, weight) VALUES'
#     '("Caio Dantas", 105.6),'
#     '("UISH Kiasn", 123.6),'
#     '("Esdu Iekm", 105.6),'
#     '("Grigo Hur", 102),'
#     '("Isadora Dantas", 78.9)'
# )

sql = (
    f'INSERT INTO {TABLE_NAME} (name, weight) VALUES (?, ?)'
)
# cursor.execute(sql, ['Caio Dantas', 78])

connection.executemany(
    sql, [
        ['Caio Dantas', 90], ['Rodrigo Greg', 189.9],
        ['Fada Dente', 21], ['Santa Ana', 87],
        ['Felino Silvestre', 79], ['Yaum Barj', 123]
    ]
)
connection.commit()

# Close my connection with DB
cursor.close()
connection.close()

if __name__ == '__main__':
    print(sql)