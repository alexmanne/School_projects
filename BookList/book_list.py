# SQL Practice

import sqlite3 as sql
import sys

def create_booklist_db():
    """Create a database called 'my_booklist.db' with two tables.

    BooksRead: Books that I have read with the following info:
        (title, author, series_name, rating, year_read)
    
    WishList: Books that I want to read with the following info:
        (title, author, series_name, recommendor)
    """

    with sql.connect("my_booklist.db") as conn:
        curs = conn.cursor()
        curs.execute("CREATE TABLE BooksRead (title TEXT, author TEXT, "
                     "series_name TEXT, rating INT, year_read INT);")

        curs.execute("CREATE TABLE WishList (title TEXT, author TEXT, "
                     "series_name TEXT, recommendor TEXT);")
        
    conn.close()

    print("Created 'my_booklist.db' with two tables")
    return


def add_book():
    return


AVAILABLE_FUNCTIONS = ("\nAvailable Functions:\n"
                       "'Create Booklist': Creates a database called 'my_booklist.db'"
                       "\n")


def main(args):
    if len(args) > 1:
        
        if args[1] == "help":
            print(AVAILABLE_FUNCTIONS)

        if args[1] == "Create Booklist":
            create_booklist_db()
        
    return


if __name__ == "__main__":
    main(sys.argv)
