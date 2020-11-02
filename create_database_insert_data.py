import sqlite3
from sqlite3 import Error


# create connection method
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


datapath = './data/'
databasename = 'AIDM7360_exercise2_movie.db'
dbConnection = create_connection(datapath + databasename)

# close the databash connection
if dbConnection:
    dbConnection.close()
    print('Connection closed')


# Create tables
def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


# Create three tables Movie, Reviewer, Rating
sql_create_Movie_table = """ CREATE TABLE IF NOT EXISTS Movies (
                                mID integer PRIMARY KEY,
                                title text NOT NULL,
                                year text,
                                director text NOT NULL
                                ); """

sql_create_Reviewer_table = """ CREATE TABLE IF NOT EXISTS Reviewer (
                                   rID integer PRIMARY KEY,
                                   name text NOT NULL
                                   ); """

sql_create_Rating_table = """ CREATE TABLE IF NOT EXISTS Rating (
                                rID integer,
                                mID integer,
                                stars integer,
                                ratingDate text,
                                PRIMARY KEY (rID, mID),
                                FOREIGN KEY (mID) REFERENCES Movies (mID),
                                FOREIGN KEY (rID) REFERENCES Reviewer (rID)
                                ); """


datapath = './data/'
databasename = 'AIDM7360_exercise2_movie.db'
dbConnection = create_connection(datapath + databasename)


# Create Tables
if dbConnection is not None:
    create_table(dbConnection, sql_create_Movie_table)
    create_table(dbConnection, sql_create_Rating_table)
    create_table(dbConnection, sql_create_Reviewer_table)
else:
    print("Error! Cannot create the database connection.!!!!!!")


# insert method
# Movies
def insert_movie(conn, movie_row):
    sql = ''' INSERT INTO Movies(title, year, director)
              VALUES(?, ?, ?) '''
    cur = conn.cursor()
    cur.execute(sql, movie_row)
    conn.commit()

    return cur.lastrowid


# Reviewer


def insert_Reviewer(conn, reviewer_row):
    sql = ''' INSERT INTO Reviewer(name)
              VALUES (?) '''
    cur = conn.cursor()
    cur.execute(sql, reviewer_row)
    conn.commit()

    return cur.lastrowid

# Rating


def insert_rating(conn, rating_row):
    sql = ''' INSERT INTO Rating(rID, mID, stars, ratingDate)
              VALUES(?, ?, ?, ?) '''
    cur = conn.cursor()
    cur.execute(sql, rating_row)
    conn.commit()

    return cur.lastrowid


datapath = './data/'
databasename = 'AIDM7360_exercise2_movie.db'
dbConnection = create_connection(datapath + databasename)
# insert the valuse
with dbConnection:
    # Moive data
    Movie1 = ('Ready Player One', '2018', 'Steven Spielberg')
    Movie2 = ('The Post', '2017', 'Steven Spielberg')
    Movie3 = ('The Lost World: Jurassic Park', '1997', 'Steven Spielberg')
    Movie4 = ('Tenet', '2020', 'Christopher Nolan')
    Movie5 = ('Dunkirk', '2017', 'Christopher Nolan')
    Movie6 = ('Inception', '2010', 'Christopher Nolan')
    Movie7 = ('Interstellar', '2014', 'Christopher Nolan')

    Movie_id1 = insert_movie(dbConnection, Movie1)
    Movie_id2 = insert_movie(dbConnection, Movie2)
    Movie_id3 = insert_movie(dbConnection, Movie3)
    Movie_id4 = insert_movie(dbConnection, Movie4)
    Movie_id5 = insert_movie(dbConnection, Movie5)
    Movie_id6 = insert_movie(dbConnection, Movie6)
    Movie_id7 = insert_movie(dbConnection, Movie7)

    # Reviewer
    # PS I don't know any reviewer so i used the character name in an amercian tv show office
    Reviewer1 = ('Michael',)
    Reviewer2 = ('Dwight',)
    Reviewer3 = ('Pam',)
    Reviewer4 = ('Jim',)
    Reviewer5 = ('Andy',)

    R_id1 = insert_Reviewer(dbConnection, Reviewer1)
    R_id2 = insert_Reviewer(dbConnection, Reviewer2)
    R_id3 = insert_Reviewer(dbConnection, Reviewer3)
    R_id4 = insert_Reviewer(dbConnection, Reviewer4)
    R_id5 = insert_Reviewer(dbConnection, Reviewer5)

    # Rating
    Rating1 = (R_id4, Movie_id1, 5, '2019')
    Rating2 = (R_id1, Movie_id2, 3, '2018')
    Rating3 = (R_id3, Movie_id3, 4, '2000')
    Rating4 = (R_id1, Movie_id4, 4, '2020')
    Rating5 = (R_id2, Movie_id5, 4, '2019')
    Rating6 = (R_id5, Movie_id6, 5, '2018')
    Rating7 = (R_id1, Movie_id7, 5, '2011')

    insert_rating(dbConnection, Rating1)
    insert_rating(dbConnection, Rating2)
    insert_rating(dbConnection, Rating3)
    insert_rating(dbConnection, Rating4)
    insert_rating(dbConnection, Rating5)
    insert_rating(dbConnection, Rating6)
    insert_rating(dbConnection, Rating7)

dbConnection.close()
