# we need to connect database from a program(python, javascript) then we need a database connector
# database connector connects your program with Database
# mysqlclient, psycopg2 are the database connector



def estd_connection():
    import psycopg2
    conn = psycopg2.connect(
        database = "studenttesttb",
        user = "postgres",
        password = "0127",
        host = "127.0.0.1",
        port = 5432
    )
    conn.autocommit = True
    print("connection established successfully! ")
    cursor= conn.cursor()
    return cursor

if __name__ == "__main__":
    estd_connection()