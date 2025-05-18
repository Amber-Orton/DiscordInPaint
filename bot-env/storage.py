import sqlite3
import os

class Storage:
    def __init__(self, db_name=None):
        if db_name is None:
            db_name = os.path.join(os.path.dirname(__file__), 'storage.db')
        self.db_name = db_name
        self.create_tables()

    def connect(self):
        return sqlite3.connect(self.db_name)

    def create_tables(self):
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS Users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                UNIQUE(username)
            )
            """)
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS Servers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )
            """)
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS Channel_groups (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                server_id INTEGER NOT NULL,
                FOREIGN KEY (server_id) REFERENCES Servers (id)
            )
            """)
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS Channels (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                server_id INTEGER,
                channel_group_id INTEGER,
                is_group_chat BOOLEAN NOT NULL,
                is_in_channel_group BOOLEAN NOT NULL,
                FOREIGN KEY (server_id) REFERENCES Servers (id)
                FOREIGN KEY (channel_group_id) REFERENCES Channel_groups (id)
            )
            """)
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS Messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                content TEXT NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                user_id INTEGER,
                channel_id INTEGER,
                is_dm BOOLEAN NOT NULL DEFAULT 0,
                FOREIGN KEY (user_id) REFERENCES Users (id),
                FOREIGN KEY (channel_id) REFERENCES Channels (id)
            )
            """)
            conn.commit()
        print("Database and tables created successfully.")