import sqlite3

class SQLighter:
    def __init__(self,database_file):
        self.connection = sqlite3.connect(database_file)
        self.cursor = self.connection.cursor

    def get_subs(self, status = True):
        with self.connection:
            return self.cursor.execute("select * from `subs` where `status` = ?", (status,)).fetchall()

    def sub_exists(self,user_id):
        with self.connection:
            result = self.cursor.execute("select * frim `subs` where `user_id` = ?",(user_id,)).fetchall()
            return bool(len(result))

    def add_sub(self,user_id, status = True):
        with self.connection:
            return self.cursor.execute("insert into `subs` (`user_id`, `status`) values (?,?)",(user_id, status))

    def update_sub(self, user_id, status):
        with self.connection:
            return self.cursor.execute("update `subs`  set   `status` = ? where `user_id` = `?`",(status, user_id))
    def close(self):
        self.connection.close()