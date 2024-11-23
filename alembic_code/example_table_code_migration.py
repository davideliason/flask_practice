import psycopg2

# Connect to your postgres DB
conn = psycopg2.connect(
    """
    dbname=week3 user=postgres host=pg port=5432
    """
)

conn.set_session(autocommit=True)

# Open a cursor to perform database operations
cur = conn.cursor()

cur.execute(
    """
    CREATE TABLE veggies(
        id SERIAL PRIMARY KEY,
        name TEXT NOT NULL,
        color TEXT NOT NULL
    )
    """
)

cur.execute(
    """
    INSERT INTO veggies VALUES 
    (1, 'carrot', 'orange'),
    (2, 'onion', 'yellow'),
    (3, 'zucchini', 'green'),
    (4, 'squash', 'yellow'),
    (5, 'pepper', 'red'),
    (6, 'onion', 'red')
    """
)

# Execute a query
cur.execute(
    """
    SELECT * FROM veggies
    """
)

# Retrieve query results
records = cur.fetchall()

print(records)
