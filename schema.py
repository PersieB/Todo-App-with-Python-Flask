import sqlite3

"""
Database to have 3 tables: users, todo list and tasks
There's a separate table for tasks because one todo list created can have multiple tasks
"""
connection = sqlite3.connect('todo_list.db', check_same_thread=False)
cursor = connection.cursor()
cursor.executescript(
    """
    CREATE TABLE users(
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        username VARCHAR(20),
        email VARCHAR(50),
        password VARCHAR(100)
    );

    CREATE TABLE todo_list(
        todo_id INTEGER PRIMARY KEY AUTOINCREMENT,
        title VARCHAR(100),
        date_created DATE,
        status VARCHAR(20) CHECK (status IN ("NOT STARTED", "IN-PROGRESS", "COMPLETED")),
        user_id INTEGER,
        FOREIGN KEY (user_id) REFERENCES users(user_id)
        
    );

    CREATE TABLE tasks(
        task_id INTEGER PRIMARY KEY AUTOINCREMENT,
        todo_id INTEGER NOT NULL,
        activity TEXT,
        status VARCHAR(20) CHECK (status IN ("NOT STARTED", "IN-PROGRESS", "COMPLETED")),
        FOREIGN KEY (todo_id) REFERENCES todo_list(todo_id)
    );
    """
)
connection.commit()
cursor.close()
connection.close()
