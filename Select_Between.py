import sqlite3
from sqlite3 import Error


def create_connection(db_file):

    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def select_Where_between_tasks_date_invoices(conn):

    cur = conn.cursor()
    cur.execute("""SELECT
                        InvoiceId,
                        BillingAddress,
                        InvoiceDate,
                        Total
                    FROM
                        invoices
                    WHERE
                        InvoiceDate BETWEEN '2010-01-01' AND '2010-01-31'

                    ORDER BY
                        InvoiceDate
    """)

    rows = cur.fetchall()

    for row in rows:
        print(row)


def main():
    database = r"D:\sqlite3\chinook.db"

    conn = create_connection(database)

    with conn:

        print("2. Query all tasks")
        select_Where_between_tasks_date_invoices(conn)


if __name__ == '__main__':
    main()
