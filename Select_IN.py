import sqlite3
from sqlite3 import Error


def create_connection(db_file):

    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def select_Where_IN_tasks(conn):

    cur = conn.cursor()
        # mediatypeid = 1 OR mediatypeid = 2 ====> mediatypeid IN (1,2)

    cur.execute("""SELECT
                        TrackId,
                        Name,
                        MediaTypeId
                  FROM
                        Tracks

                    WHERE
                        AlbumId IN (

                        SELECT
                            AlbumId
                        FROM
                            Albums
                        WHERE
                            ArtistId = 12

                        )
    """)

    rows = cur.fetchall()

    for row in rows:
        print(row)


def main():
    database = r"D:\sqlite3\chinook.db"

    conn = create_connection(database)

    with conn:

        print("2. Query all tasks")
        select_Where_IN_tasks(conn)


if __name__ == '__main__':
    main()
