import sqlite3
from sqlite3 import Error


def create_connection(db_file):

    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def select_Where_LIKE(conn):

    cur = conn.cursor()
        #LIKE 'TE%' , '%TE' ,'%TE%', TEXT --> TE_T



#   cur.excute("""SELECT 
#                   track_id,
#                   name
#                 From
#                   tracks
#                 WHERE
#                   name LIKE  '%Wild'
#   
#   """



    # cur.execute("""SELECT
    #                         l.Title,
    #                         r.Name
    #                     FROM
    #                         albums l
    #                     INNER JOIN artists r
    #                         ON r.ArtistId = l.ArtistId;
    # #
    # """)


    # cur.execute("""    SELECT
                        #     Title,
                        #     Name
                        # FROM
                        #     albums
                        # INNER JOIN artists USING(ArtistId)
    # """)


    cur.execute("""SELECT
                        title,
                        Name
                    FROM
                        albums
                    INNER JOIN artists
                        ON artists.ArtistId = albums.ArtistId;

    """)

    rows = cur.fetchall()

    for row in rows:
        print(row)


def main():
    database = r"D:\sqlite3\chinook.db"

    conn = create_connection(database)

    with conn:

        print("2. Query all tasks")
        select_Where_LIKE(conn)


if __name__ == '__main__':
    main()
