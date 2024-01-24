import sqlite3
from uuid import uuid4
from datetime import datetime

class Task_DB():

    def __init__(self):
        self.connection = self.create_connection("./db/tasks.db")
        self.cursor = self.connection.cursor()

        self.create_table()


    def create_connection(self, path):
        connection = None
        try:
            connection = sqlite3.connect(path)
            print("Connection to SQLite DB successful")
        except sqlite3.Error as e:
            print(f"The error '{e}' occurred")
            exit()
        return connection
    
    def create_table(self):
        listOfTables = self.cursor.execute("""SELECT 1 FROM sqlite_master WHERE type='table' AND name='TASKS'; """).fetchall()
 
        if listOfTables == []:           
            self.cursor.execute("""CREATE TABLE TASKS(TITLE TEXT, OWNER_ID INTEGER, DESCRIPTION TEXT, TASK_ID TEXT, DATE_CREATED INTEGER, DATE_DUE INTEGER, COMPLETED INTEGER, ACCESS TEXT);""")
        else:
            print('Table found!')

    def close_connection(self):
        self.connection.close()


class Task():

    def __init__(self, title, owner: int, description, date_due):
        self.title = title
        self.owner_id = owner
        self.description = description
        self.task_id = str(uuid4())
        self.date_created = (datetime.now() - datetime(1970, 1, 1)).total_seconds()
        self.date_due = (date_due - datetime(1970, 1, 1)).total_seconds()
        self.completed = False
        self.access = None

class User():

    def __init__(self):
        self.username = None
        self.email = None
        self.user_id = None
        self.date_joined = None
        self.last_login = None
        self.password_sha256 = None