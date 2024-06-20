# This program generates a random database, takes in an INT, and injects fake data into sqlite3 databases
import sqlite3
from faker import Faker

# Database Variable with Faker module
fake = Faker()
db_name = fake.color_name() + ".db"

# Arrays for Tables
users_data = []
posts_data = []

# SQL for Tables
sql_commands = ["""CREATE TABLE users (                
    table_id INTEGER PRIMARY KEY,
    full_name VARCHAR(30),
    email VARCHAR(30) )""",

    """CREATE TABLE posts (
    posts_id INTEGER PRIMARY KEY,
    published DATE,
    post_content TEXT )""",]

# Functions to Insert into Tables
def insert_users(connection, int):
    # Create Faker Data
    for _ in range(int):
        user_name = fake.name_nonbinary()
        user_email = fake.email()
        user_data = [user_name, user_email]
        # Append to Table Array
        users_data.append(user_data)
    # Iterates over Users Data and Inserts into Users Table
    for i in range(len(users_data)):
        user_fullname = users_data[i][0]
        user_email = users_data[i][1]  
        # Execute Insert    
        cursor = connection.cursor() 
        cursor.execute("""INSERT INTO users(full_name, email) VALUES (?, ?) """, (user_fullname, user_email))
        connection.commit()           

def insert_posts(connection, int):
    for _ in range(int):
        # Create Faker Data
        published_date = fake.date()
        post_content = fake.text()
        post_data = [published_date, post_content]
        # Append to Table Array
        posts_data.append(post_data)        
    # Iterates over Posts Data and Inserts into Posts Table
    for i in range(len(posts_data)):
        # Create Faker Data
        posts_date = posts_data[i][0]
        posts_content = posts_data[i][1]
        # Execute Insert
        cursor = connection.cursor()  
        cursor.execute("""INSERT INTO posts(published, post_content) VALUES (?, ?) """, (posts_date, posts_content))  
        connection.commit()

# Fetch with SQL SELECT *
fetch_commands = [
    """SELECT * FROM users """,
    """SELECT * FROM posts """]
def get_database(connection):
    for fetch_command in fetch_commands:
            cursor = connection.cursor()
            cursor.execute(fetch_command)   
            # Store all the data
            results = cursor.fetchall()
            print("Table: ", results)
   
# Create Database Connection
def main():
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            # Create Tables
            for sql_command in sql_commands:
                cursor.execute(sql_command)
            # Select Number to Insert Users
            number = 100
            insert_users(connection, number) 
            # Select Number to Insert Posts
            number = 100
            insert_posts(connection, number)
            # Fetch Database
            database = "Pink.db"
            get_database(connection)   

    except sqlite3.Error as e:
        print(e)
    finally:
        if connection:
            connection.close()

if __name__ == '__main__':
    main()