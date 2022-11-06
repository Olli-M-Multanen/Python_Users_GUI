import pandas as pd
from getpass import getpass
import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    
    return conn

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def select_all_users(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * from users")

    rows = cur.fetchall()
    for row in rows:
        print(row)

def main():
    database = r"database.db"

    sql_create_users_table = """ CREATE TABLE IF NOT EXISTS users (

                                id INTEGER NOT NULL PRIMARY KEY,
                                firstname TEXT NOT NULL,
                                lastname TEXT NOT NULL,
                                age INT NOT NULL,
                                profession TEXT,
                                adress TEXT,
                                city TEXT
                                );"""

    # create a database connection
    conn = create_connection(database)

    # create table
    with conn:
        print("- All users in database:")
        select_all_users(conn)

    # Take excel file and read it with panda
    input_file = "base.xlsx"

    users = pd.read_excel(input_file,
        sheet_name = "Sheet1",
        header = 0,
        index_col = False,
        keep_default_na = True
    )

    # create dataframe from it
    df = pd.DataFrame(users, columns = ['firstName', 'lastName', 'age', 'profession', 'adress', 'city'])

    # Connect to already created database and inject dataframe to it
    df.to_sql('users', conn, if_exists='replace', index = False)


if __name__ == '__main__':
    main()
