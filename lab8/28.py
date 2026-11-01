import sqlite3

try:
    conn = sqlite3.connect("students.db")
    conn.execute("SELECT * FROM table_that_does_not_exist")
except sqlite3.Error as error:
    print("Database error:", error)
finally:
    if "conn" in locals():
        conn.close()