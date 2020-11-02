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

with dbConnection:
    # New movies
    Movie8 = ('Mulan', '2020', 'Niki Caro')
    Movie9 = ('Cats', '2019', 'Tom Hooper')
    Movie10 = ('Jack and Jill', '2011', 'Adam Sandler')
    Movie11 = ('The Room', '2003', 'Tommy Wiseau')
    Movie12 = ('dummy1', '2000', 'dummy')
    Movie13 = ('dummy2', '2000', 'dummy')
    Movie14 = ('Gone with the Wind', '1952', 'Victor Fleming')

    Movie_id8 = insert_movie(dbConnection, Movie8)
    Movie_id9 = insert_movie(dbConnection, Movie9)
    Movie_id10 = insert_movie(dbConnection, Movie10)
    Movie_id11 = insert_movie(dbConnection, Movie11)
    Movie_id12 = insert_movie(dbConnection, Movie12)
    Movie_id13 = insert_movie(dbConnection, Movie13)
    Movie_id14 = insert_movie(dbConnection, Movie14)

    # new reviewer
    Reviewer6 = ('Jason',)
    Reviewer7 = ('Andrewson',)
    Reviewer8 = ('Andrew',)
    Reviewer9 = ('Chris Jackson',)
    Reviewer10 = ('Nobody',)
    Reviewer11 = ('NO THIS PERSON',)

    R_id6 = insert_Reviewer(dbConnection, Reviewer6)
    R_id7 = insert_Reviewer(dbConnection, Reviewer7)
    R_id8 = insert_Reviewer(dbConnection, Reviewer8)
    R_id9 = insert_Reviewer(dbConnection, Reviewer9)
    R_id10 = insert_Reviewer(dbConnection, Reviewer10)
    R_id11 = insert_Reviewer(dbConnection, Reviewer11)

    # new ratings
    Rating8 = (R_id9, Movie_id8, 3, '2020')
    Rating9 = (R_id9, Movie_id9, 1, '2020')
    Rating10 = (R_id9, Movie_id10, 2, '2012')
    Rating11 = (R_id7, Movie_id11, 1, None)
    Rating12 = (R_id6, Movie_id12, None, None)
    Rating13 = (R_id8, Movie_id13, None, None)
    Rating13 = (R_id6, Movie_id14, None, None)
    Rating14 = (R_id7, Movie_id14, 2, '2020')
    Rating15 = (R_id8, Movie_id14, 5, '1990')
    Rating16 = (R_id9, Movie_id14, 5, '2009')

    insert_rating(dbConnection, Rating8)
    insert_rating(dbConnection, Rating9)
    insert_rating(dbConnection, Rating10)
    insert_rating(dbConnection, Rating11)
    insert_rating(dbConnection, Rating12)
    insert_rating(dbConnection, Rating13)
    insert_rating(dbConnection, Rating14)
    insert_rating(dbConnection, Rating15)
    insert_rating(dbConnection, Rating16)

dbConnection.close()
