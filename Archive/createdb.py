import sqlite3

from sqlite3 import Error

def sql_connection():
    try:

        con = sqlite3.connect('BunnyBarn.db')

        return con

    except Error:

        print(Error)

def sql_table(con):
    cursorObj = con.cursor()

    cursorObj.execute("CREATE TABLE breeds(id integer PRIMARY KEY NOT NULL UNIQUE, name text, abv text)")

    con.commit()

con = sql_connection()

sql_table(con)
