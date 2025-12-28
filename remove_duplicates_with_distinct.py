import sqlite3

def remove_duplicates_with_distinct():
    # Connect to a local SQLite database (example.db)
    conn = sqlite3.connect("example.db")
    cursor = conn.cursor()

    # SQL query for Challenge #5
    query = "SELECT DISTINCT category FROM products"

    cursor.execute(query)
    rows = cursor.fetchall()

    # Print results
    for row in rows:
        print(row)

    conn.close()


if __name__ == "__main__":
    remove_duplicates_with_distinct()
