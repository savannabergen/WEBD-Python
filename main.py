## Savanna Bergen/WEBD-3010  
import sqlite3
from faker import Faker

# variable for database name
fake = Faker()
db_name = fake.color_name() + ".db"

# array of commands to create tables
sql_commands = ["""CREATE TABLE users (                
    users_id INTEGER PRIMARY KEY,
    full_name VARCHAR(30),
    email VARCHAR(30) )""",

    """CREATE TABLE posts (
    posts_id INTEGER PRIMARY KEY,
    published DATE,
    post_content TEXT )""",

    """CREATE TABLE user_info (
    comment_id INTEGER PRIMARY KEY,
    users_id INTEGER,
    users_country VARCHAR(30),
    FOREIGN KEY(users_id) REFERENCES users(users_id) )"""]

# method to insert users
def simple_insert_users(conn, user):
    sql = ("""INSERT INTO users(full_name, email) VALUES(?, ?) """)
    cur = conn.cursor()
    cur.execute(sql, user)
    conn.commit()
    return cur.lastrowid

# method to insert posts
def simple_insert_posts(conn, post):
    sql = ("""INSERT INTO posts(published, post_content) VALUES(?, ?) """)
    cur = conn.cursor()
    cur.execute(sql, post)
    conn.commit()
    return cur.lastrowid

# method to insert info
def simple_insert_info(conn, info):
    sql = ("""INSERT INTO user_info(users_id, users_country) VALUES(?, ?) """)
    cur = conn.cursor()
    cur.execute(sql, info)
    conn.commit()
    return cur.lastrowid

# main method to execute
def main():
    try:
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            for sql_command in sql_commands:
                cursor.execute(sql_command)
            # add new user
            users = [('Savanna', 'ss@gmail'), ('John Doe', 'joe@yahoo.ca'), ('George Little', 'glittle@hotmail.com')]
            for user in users:
                user_id = simple_insert_users(conn, user)

            # add a new post
            posts = [('This is some content', '6-17-2024'), ('YES TEXT', '6-16-2024'), ('And Again', '6-15-2024')]

            for post in posts:
                simple_insert_posts(conn, post)

            # add a new comment
            information = [(user_id, 'China'), (user_id, 'Russia'), (4, 'USA')]

            for info in information:
                simple_insert_info(conn, info)

        # display users from database
        sql = ("""SELECT * FROM users """)
        cursor.execute(sql)   
        # Store all the data
        results = cursor.fetchall()
        print("User's Table: ", results)
        conn.commit()

        # display posts from database
        sql = ("""SELECT * FROM posts """)
        cursor.execute(sql)   
        # Store all the data
        results = cursor.fetchall()
        print("Post's Table: ", results)
        conn.commit()

        # display user_info from database
        sql = ("""SELECT * FROM user_info """)
        cursor.execute(sql)   
        # Store all the data
        results = cursor.fetchall()
        print("User's Info Table: ", results)
        conn.commit()

        # update database
        update_statement = 'UPDATE users SET full_name=?, email=? WHERE users_id =?'
        cursor.execute(update_statement, ("Troy", "LULZGUY!", 1))
        cursor.execute('''SELECT * FROM users WHERE full_name='Troy' ''')
        results = cursor.fetchall()
        conn.commit()
        print("Updated (Replaced User 'Savanna' with an id of 1: ", results)

        # delete database
        cursor.execute('''DELETE FROM user_info WHERE users_id='4' ''')
        cursor.execute('''SELECT * FROM user_info ''')
        results = cursor.fetchall()
        print("Deleted User's with a users_ID of 4:", results)    

    # catch error, close connection
    except sqlite3.Error as e:
        print(e)
    finally: 
        if conn:
            conn.close() 

# call main method
if __name__ == '__main__':
    main()

