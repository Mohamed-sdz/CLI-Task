# database.py

import sqlite3

def create_connection():
    # Create a connection to the database
    conn = sqlite3.connect('tasks.db')
    return conn

def create_tables(conn):
    # Create necessary tables if they don't exist
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            description TEXT,
            priority TEXT,
            due_date TEXT,
            status TEXT
        )
    ''')
    conn.commit()

def insert_task(conn, task_data):
    # Insert a new task into the database
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO tasks (title, description, priority, due_date, status)
        VALUES (?, ?, ?, ?, ?)
    ''', task_data)
    conn.commit()

def get_all_tasks(conn):
    # Retrieve all tasks from the database
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tasks')
    return cursor.fetchall()

# Add more database functions as needed
