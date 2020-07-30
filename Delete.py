import sqlite3
from sqlite3 import Error


def create_connection(db_file):

    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def delete_task_where(conn, id):

    sql = 'DELETE FROM tasks WHERE id = ?'
    cur = conn.cursor()
    cur.execute(sql,(id,))
    conn.commit()

def delete_all_tasks(conn):
    sql = 'DELETE FROM tasks'
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()


def main():

    database = r"D:\sqlite3\pythonsqlite.db"

    conn = create_connection(database)

    with conn:
        # delete_task_where(conn,2)
        delete_all_tasks(conn)

if __name__ == '__main__':
    main()