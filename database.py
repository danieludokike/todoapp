
import sqlite3


def connect():
    conn = sqlite3.connect("todo.db")
    return conn


def create_table():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        completed INTEGER DEFAULT 0
    )
    """)
    conn.commit()
    conn.close()
    

def add_task(title):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (title) VALUES (?)", (title,))
    conn.commit()
    conn.close()
    
def get_tasks():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    conn.close()
    return tasks

def complete_task(task_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET completed = 1 WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
    
def delete_task(task_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()