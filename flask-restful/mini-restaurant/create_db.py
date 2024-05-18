import sqlite3

# Establish a connection
connection = sqlite3.connect('restaurant.db')
cursor = connection.cursor()

# create table for users
create_table_users = "CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY,username text,password text)"
cursor.execute(create_table_users)

# create table for food
create_table_food = "CREATE TABLE IF NOT EXISTS food(id INTEGER PRIMARY KEY, name text,type text,ingredient text,amount text)"
cursor.execute(create_table_food)

# create table for menu
create_table_menu = "CREATE TABLE IF NOT EXISTS menu(id INTEGER PRIMARY KEY, name text,type text,price real)"
cursor.execute(create_table_menu)

# create table for order
create_table_order = "CREATE TABLE IF NOT EXISTS order(id INTEGER PRIMARY KEY, name text,description text,amount text,price text)"
cursor.execute(create_table_order)

# create table for recipe
create_table_recipe = "CREATE TABLE IF NOT EXISTS recipe(id INTEGER PRIMARY KEY, name text,ingredient text,amount text)"
cursor.execute(create_table_recipe)

# close the connecton
connection.commit()
connection.close()