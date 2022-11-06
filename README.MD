example project.

Idea is to take sample excel file, and transfer all the data
to SQLite database, using Pandas Dataframes.

Display data with a Tkinter widget

Plan of action

1. Create .excel file containing dummy data - RAS

2. copy data to Pandas Dataframe - RAS


3. Create a SQLite database "database". - RAS

    CREATE DATABASE database

4. Create SQLite table "users". - RAS

python command

Database table schema:

CREATE TABLE IF NOT EXISTS users(
    id INTEGER NOT NULL PRIMARY KEY,
    firstname TEXT NOT NULL,
    lastname TEXT NOT NULL,
    age INT NOT NULL,
    profession TEXT,
    adress TEXT,
    city TEXT
);


5. Copy Dataframe to MySQL. - RAS

6. Create a Tkinter widget to display MySQL table data - not there yet

7. Add functionality to widget (add, remove, edit) - not there yet
