# Import psycopg2 package
import psycopg2

def create_connection(host, port, user, password, dbname):
    """
    Establish a connection to the postgresql database
    returns a "connection" class to be used by all other functions
    """
    conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
    return conn

def close_connection(conn):
    """
    Closes an open connection to the database
    """
    conn.close()

def execute_query(conn, query:str):
    """
    Execute a non-scalar query on the open given connection
    """

    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()

    # Executing a query
    cursor.execute(query)

    # Commit the changes inside the database and close the connection
    conn.commit()    


def select_data(conn, select_query):
    """
    Performs a select query returns the fetchall records
    """    
    cursor = conn.cursor()
    cursor.execute(select_query)

    # Fetch e all rows from the result set
    rows = cursor.fetchall()

    return rows


CREATE_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS test_users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    age INTEGER CHECK (age >= 0),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""

if __name__=="__main__":
    # Replace these with your database credentials
    dbname = "postgres"
    user = "postgres.your-tenant-id"
    password = "R3vyPCrVN0sMYdklJ2Rp13Y5"
    host = "localhost"
    port = "5432"

    conn = create_connection(host, port, user, password, dbname)
    execute_query(conn, CREATE_TABLE_QUERY)
    insert = "insert into test_users (name, email, age) values ('jim132', 'jim132@kuki.com', 26);"
    execute_query(conn, insert)

    rows = select_data(conn, "SELECT * FROM test_users;")
    for r in rows:
        print(r)
    close_connection(conn)