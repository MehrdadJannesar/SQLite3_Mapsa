import sqlite3
from sqlite3 import Error


def create_connection(db_file):

    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def update_task(conn, task):

    sql = '''
            UPDATE tasks

            SET priority = ?,
            begin_date = ?,
            end_date = ?
            WHERE id = ?
    '''

    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()

def main():

    database = r"D:\sqlite3\pythonsqlite.db"

    conn = create_connection(database)
    with conn:
        update_task(conn, (3, '2020-01-08', '2020-01-10', 2))


if __name__ == '__main__':
    main()
