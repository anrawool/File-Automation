import sqlite3
from typing import Any

class DBManager:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.cur = self.conn.cursor()

    def execute_query(self, query, details=None):
        if details != None:
            self.cur.execute(query, details)
        else:
            self.cur.execute(query)
        
    @property
    def get_connection(self):
        return self.conn, self.cur

