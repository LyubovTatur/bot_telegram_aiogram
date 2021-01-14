import sqlite3

class SQLighter:
    def __init__(self,database_file):
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor

    def get_subs(self, status = True):
        with self.connection:
            return self.cursor.execute("select * from 'subs' where 'status' = {}".format(status))

    def sub_exists(self,user_id):

