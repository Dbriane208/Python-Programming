import sqlite3

# Establish the connection
connection = sqlite3.connect('data.db')
cursor = connection.cursor()

# creating a table users if it doesn't exist
create_table_users = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_table_users)

# creating a table for items
create_table_items = "CREATE TABLE IF NOT EXISTS items (name text,price real)"
cursor.execute(create_table_items)

# closing the connection
connection.commit()
connection.close()