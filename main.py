# PyMySQL - um cliente MySQL feito em Python Puro
# Doc: https://pymysql.readthedocs.io/en/latest/
# Pypy: https://pypi.org/project/pymysql/
# GitHub: https://github.com/PyMySQL/PyMySQL
import os

import pymysql
import dotenv

TABLE_NAME = 'customers'

dotenv.load_dotenv()

connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],
)
with connection:
    with connection.cursor() as cursor:
        cursor.execute(
            f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ( '
            'id INT NOT NULL AUTO_INCREMENT, '
            'nome VARCHAR(50) NOT NULL, '
            'idade INT NOT NULL, '
            'PRIMARY KEY (id) '
            ') '
        )
        cursor.execute(f'TRUNCATE TABLE {TABLE_NAME}')
        connection.commit()

        with connection.cursor() as cursor:
            results = cursor.execute(
                f'INSERT INTO {TABLE_NAME} (nome, idade) '
                'VALUES ("Caio", 20) '
            )
            print(results)
            connection.commit()
