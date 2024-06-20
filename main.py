import sqlite3
from faker import Faker

fake = Faker()
db_name = fake.color_name() + ".db"

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

# fetch all rows from tables in database
def display_database(conn):
    fetch_commands = [
    """SELECT * FROM users """,
    """SELECT * FROM posts """, 
    """SELECT * FROM user_info """]
    cur = conn.cursor()

    for fetch_command in fetch_commands:
        cur.execute(fetch_command)   
        # Store all the data
        results = cur.fetchall()
        print("Table: ", results)
    conn.commit()
    return cur.lastrowid

# main method to execute
def main():
    try:
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            for sql_command in sql_commands:
                cursor.execute(sql_command)
        print(db_name)
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

        # display database
        display_database(conn)

        # update database
        update_statement = 'UPDATE users SET full_name=?, email=? WHERE users_id =?'
        cursor.execute(update_statement, ("Troy", "LULZGUY!", 1))
        cursor.execute('''SELECT * FROM users ''')
        results = cursor.fetchall()
        conn.commit()
        print("Updated:", results)

        # delete database
        cursor.execute('''DELETE FROM user_info WHERE users_id='3' ''')
        cursor.execute('''SELECT * FROM user_info ''')
        results = cursor.fetchall()
        print("Deleted:", results)    

    # catch error, close connection
    except sqlite3.Error as e:
        print(e)
    finally: 
        if conn:
            conn.close() 

# call main method
if __name__ == '__main__':
    main()

