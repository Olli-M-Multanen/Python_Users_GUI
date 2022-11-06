import pandas as pd
from getpass import getpass
import sqlite3
from sqlite3 import Error

from tkinter import *

root = Tk()

# Entry Widgets
fnameEntry = Entry(root, width=20, bg="gray", fg="white")
lnameEntry = Entry(root, width=20, bg="gray", fg="white")
ageEntry = Entry(root, width=20, bg="gray", fg="white")
professionEntry = Entry(root, width=20, bg="gray", fg="white")
streetEntry = Entry(root, width=20, bg="gray", fg="white")
cityEntry = Entry(root, width=20, bg="gray", fg="white")


def myClick():
    rapportBanner = Label(root, text="New User").grid(row=10, column=0)

    userNames = fnameEntry.get() +" " + lnameEntry.get()
    namesBanner = Label(root, text="User").grid(row=11, column=0)
    userNamesLabel = Label(root, text=userNames).grid(row=11, column=1)

    userAge = ageEntry.get()
    AgeBanner = Label(root, text="Age").grid(row=12, column=0)
    userNamesLabel = Label(root, text=userAge).grid(row=12, column=1)

    userProfession = professionEntry.get()
    professionBanner = Label(root, text="Profession").grid(row=13, column=0)
    userProfessionLabel = Label(root, text=userProfession).grid(row=13, column=1)

    userStreet = streetEntry.get()
    userCity = cityEntry.get()
    streetBanner = Label(root, text="Street adress").grid(row=14, column=0)
    userStreetLabel = Label(root, text=userStreet).grid(row=14, column=1)
    cityBanner = Label(root, text="City").grid(row=15, column=0)
    userCityLabel = Label(root, text=userCity).grid(row=15, column=1)

    # Add somekind of a filler text here to create space

    # Add function to dbEntryButton

    dbEntryButton = Button(root, text="Save to database", padx=10, pady=10).grid(row=16, column=0)

# Label Widgets
myBanner = Label(root, text="New Entry")
fnameLabel = Label(root, text="First Name")
lnameLabel = Label(root, text="Last Name")
ageLabel = Label(root, text="Age")
professionLabel = Label(root, text="Profession")
adressLabel = Label(root, text="Street")
cityLabel = Label(root, text="City")

myButton = Button(root, text="Submit", padx=10, pady=10, command=myClick)

# Widget positions
myBanner.grid(row=0, column=0)
fnameLabel.grid(row=1, column=0)
fnameEntry.grid(row=2, column=0)

lnameLabel.grid(row=1, column=1)
lnameEntry.grid(row=2, column=1)

ageLabel.grid(row=3, column=0)
ageEntry.grid(row=4, column=0)

professionLabel.grid(row=5, column=0)
professionEntry.grid(row=6, column=0)

adressLabel.grid(row=7, column=0)
streetEntry.grid(row=8, column=0)

cityLabel.grid(row=7, column=1)
cityEntry.grid(row=8, column=1)

myButton.grid(row=9, column=0)

root.mainloop()



# def create_connection(db_file):
#     """ create a database connection to the SQLite database
#         specified by db_file
#     :param db_file: database file
#     :return: Connection object or None
#     """
#     conn = None
#     try:
#         conn = sqlite3.connect(db_file)
#     except Error as e:
#         print(e)
    
#     return conn

# def create_table(conn, create_table_sql):
#     """ create a table from the create_table_sql statement
#     :param conn: Connection object
#     :param create_table_sql: a CREATE TABLE statement
#     :return:
#     """
#     try:
#         c = conn.cursor()
#         c.execute(create_table_sql)
#     except Error as e:
#         print(e)

# def select_all_users(conn):
#     """
#     Query all rows in the tasks table
#     :param conn: the Connection object
#     :return:
#     """
#     cur = conn.cursor()
#     cur.execute("SELECT * from users")

#     rows = cur.fetchall()
#     for row in rows:
#         print(row)

# def main():
#     database = r"database.db"

#     sql_create_users_table = """ CREATE TABLE IF NOT EXISTS users (

#                                 id INTEGER NOT NULL PRIMARY KEY,
#                                 firstname TEXT NOT NULL,
#                                 lastname TEXT NOT NULL,
#                                 age INT NOT NULL,
#                                 profession TEXT,
#                                 adress TEXT,
#                                 city TEXT
#                                 );"""

#     # create a database connection
#     conn = create_connection(database)

#     # create table
#     with conn:
#         print("- All users in database:")
#         select_all_users(conn)

#     # Take excel file and read it with panda
#     input_file = "base.xlsx"

#     users = pd.read_excel(input_file,
#         sheet_name = "Sheet1",
#         header = 0,
#         index_col = False,
#         keep_default_na = True
#     )

#     # create dataframe from it
#     df = pd.DataFrame(users, columns = ['firstName', 'lastName', 'age', 'profession', 'adress', 'city'])

#     # Connect to already created database and inject dataframe to it
#     df.to_sql('users', conn, if_exists='replace', index = False)


# if __name__ == '__main__':
#     main()
