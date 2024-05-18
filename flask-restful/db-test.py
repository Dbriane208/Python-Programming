import sqlite3

# create connection
connection = sqlite3.Connection('test.db')

# create a cursor
cursor = connection.cursor()

# create a table
create_table = "CREATE TABLE users (id int,username text, password text)"
cursor.execute(create_table)

# add user to the table
user = (1,"job","qwerty")

# insert the query
insert_query = "INSERT INTO users VALUES (?,?,?)"
users = [
    (2,"Qu","min-son"),
    (3,"Doku","Jeremy")
]
cursor.execute(insert_query,user)
cursor.executemany(insert_query,users)

# printing the users in the database
# select_query = "SELECT * FROM users"
# for row in cursor.execute(select_query):
#     print(row)


# closing the database
connection.commit()
connection.close()    