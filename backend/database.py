```python
import sqlite3
from sqlite3 import Error

def create_connection():
    conn = None;
    try:
        conn = sqlite3.connect(':memory:') # creates a database in RAM
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def main():
    database = r"C:\sqlite\db\pythonsqlite.db"

    sql_create_products_table = """ CREATE TABLE IF NOT EXISTS products (
                                        id integer PRIMARY KEY,
                                        product_name text NOT NULL,
                                        description text,
                                        product_number text,
                                        vendor_name text,
                                        cost real,
                                        product_image text,
                                        product_site text
                                    ); """

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create products table
        create_table(conn, sql_create_products_table)
    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    main()
```