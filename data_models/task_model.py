"""
The methods below perform data model operations on the tasks table
"""

import sqlite3

# Show all tasks of a particular todo item
def show_task(todo_id):
    connection = sqlite3.connect('todo_list.db', check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute(
        """
        SELECT * FROM tasks where todo_id='{todo_id}' ORDER BY task_id DESC;
        """.format(todo_id=todo_id)
    )
    tasks = cursor.fetchall()
    connection.commit()
    cursor.close()
    connection.close()
    return tasks


# Select the todo a particular task belongs to
def select_todo_in_tasks(task_id):
    connection = sqlite3.connect('todo_list.db', check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute(
        """
        SELECT todo_id FROM tasks where task_id='{task_id}';
        """.format(task_id=task_id)
    )
    todoid = cursor.fetchone()[0]
    connection.commit()
    cursor.close()
    connection.close()
    return todoid


# Add a new task activity. The default status is set as "NOR STARTED" initially, with the user checking off a different status to update when necessary
def add_task(todo_id, activity):
    status= "NOT STARTED"  #default
    connection = sqlite3.connect('todo_list.db', check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute(
        """
        INSERT into tasks(todo_id, activity, status) values('{todo_id}', '{activity}', '{status}');
        """.format(todo_id=todo_id,activity=activity,status=status)
    )
    connection.commit()
    cursor.close()
    connection.close()


# Update task activity name
def update_activityname(activity, task_id):
    connection = sqlite3.connect('todo_list.db', check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute(
        """
        UPDATE tasks set activity = '{activity}' WHERE task_id='{task_id}';
        """.format(activity=activity,task_id=task_id)
    )
    connection.commit()
    cursor.close()
    connection.close()


# Update status if user checks off a different option ("NOT STARTED, IN-PROGRESS, COMPLETED")
def update_status(status, task_id):
    connection = sqlite3.connect('todo_list.db', check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute(
        """
        UPDATE tasks set status = '{status}' WHERE task_id='{task_id}';
        """.format(status=status,task_id=task_id)
    )
    connection.commit()
    cursor.close()
    connection.close()


# Delete task
def delete_task(task_id):
    connection = sqlite3.connect('todo_list.db', check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute(
        """
        DELETE FROM tasks WHERE task_id='{task_id}';
        """.format(task_id=task_id)
    )
    connection.commit()
    cursor.close()
    connection.close()


# Delete all tasks associated with a todo item. This only happens when a todo item is completely deleted from the dashboard. It goes on to delete its associated tasks here
def delete_alltodo_tasks(todo_id):
    connection = sqlite3.connect('todo_list.db', check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute(
        """
        DELETE FROM tasks WHERE todo_id='{todo_id}';
        """.format(todo_id=todo_id)
    )
    connection.commit()
    cursor.close()
    connection.close()


# Returns current statuses of all tasks for a particular todo item.
def all_todo_task_statuses(todo_id):
    connection = sqlite3.connect('todo_list.db', check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute(
        """
        SELECT status FROM tasks WHERE todo_id='{todo_id}';
        """.format(todo_id=todo_id)
    )
    statuses = cursor.fetchall()
    connection.commit()
    cursor.close()
    connection.close()
    return statuses



        