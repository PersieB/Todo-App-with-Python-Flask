"""
The methods below perform data model operations on the todo_list table
"""

import sqlite3
import time

# Show all todos of a particular user
def show_todos(user_id):
    connection = sqlite3.connect('todo_list.db', check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute(
        """
        SELECT * FROM todo_list WHERE user_id = '{user_id}' ORDER BY todo_id DESC;
        """.format(user_id=user_id)
    )
    all_todos = cursor.fetchall()
    connection.commit()
    cursor.close()
    connection.close()
    return all_todos


# Select all todo details under consideration
def select_one(todo_id):
    connection = sqlite3.connect('todo_list.db', check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute(
        """
        SELECT * FROM todo_list WHERE todo_id = '{todo_id}';
        """.format(todo_id=todo_id)
    )
    todo= cursor.fetchone()
    connection.commit()
    cursor.close()
    connection.close()
    return todo


# Add a new todo item. Status is set to "NOT STARTED" at default. Depending on the statuses of its associated tasks, the status here automatically updates.

def add_todo(title, user_id):
    date_created=time.strftime('%Y-%m-%d')
    status= "NOT STARTED"  #default
    connection = sqlite3.connect('todo_list.db', check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute(
        """
        INSERT into todo_list(title, date_created, status, user_id) values('{title}', '{date_created}', '{status}', '{user_id}');
        """.format(title=title,date_created=date_created,status=status, user_id=user_id)
    )
    connection.commit()
    cursor.close()
    connection.close()


# Update todo title
def update_todo(title, todo_id):
    connection = sqlite3.connect('todo_list.db', check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute(
        """
        UPDATE todo_list set title = '{title}' WHERE todo_id='{todo_id}';
        """.format(title=title,todo_id=todo_id)
    )
    connection.commit()
    cursor.close()
    connection.close()


# Update todo status
def update_todo_status(status, todo_id):
    connection = sqlite3.connect('todo_list.db', check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute(
        """
        UPDATE todo_list set status = '{status}' WHERE todo_id='{todo_id}';
        """.format(status=status,todo_id=todo_id)
    )
    connection.commit()
    cursor.close()
    connection.close()


# Delete todo item
def delete_todo(todo_id):
    connection = sqlite3.connect('todo_list.db', check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute(
        """
        DELETE FROM todo_list WHERE todo_id='{todo_id}';
        """.format(todo_id=todo_id)
    )
    connection.commit()
    cursor.close()
    connection.close()


"""
Automatically updates status of Todo item based on the current status of its associated tasks
It is set to "NOT STARTED" when there are no tasks under the item, or when all tasks have their statuses NOT STARTED
It is set to COMPPLETED when all its tasks have been checked as COMPLETED
It is set as IN-PROGRESS when some tasks have at least been checked as "IN-PROGRESS" or "COMPLETED" and others remain "NOT STARTED"
"""
def check_progress(statuses):
    statlist=[]
    for i in range(len(statuses)):
        statlist.append(statuses[i][0])

    if all(elem == "NOT STARTED" for elem in statlist):
        todo_status = "NOT STARTED"

    elif all(elem == "COMPLETED" for elem in statlist):
        todo_status = "COMPLETED"

    else:
        todo_status= "IN-PROGRESS"
    
    return todo_status