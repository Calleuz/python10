import sqlite3


class Database:

    def __init__(self,db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS task(id INTEGER PRIMARY KEY, title text, category text, description text)")
        self.conn.commit()


    def insert(self, title, category, description):
        self.cur.execute("INSERT INTO task VALUES(NULL,?,?,?)",(title, category, description))
        self.conn.commit()


    def view(self):
        self.cur.execute("SELECT * FROM task")
        rows = self.cur.fetchall()
        return rows

    def search(self, title="", category = "", description = ""): #Empty strings, annars kräven funktionen alltid 4 parametrar fastän användaren endast söker efter en enda
        self.cur.execute("SELECT * FROM task WHERE title = ? OR category = ? OR description = ?", (title, category, description))
        rows = self.cur.fetchall()
        return rows

    def delete(self, id):
        self.cur.execute("DELETE FROM task WHERE id =?",(id,))
        self.conn.commit()

    def delete_latest(self):
        self.cur.execute("DELETE FROM task WHERE id = (SELECT MAX(id) FROM task)")
        self.conn.commit()




    # def update(self,id, title, author, year, isbn):
    #     self.cur.execute("UPDATE task SET title = ?, author = ?, year = ?, isbn = ? WHERE id = ?",(title, author, year, isbn, id))
    #     self.conn.commit()

    def __del__(self):
        self.conn.close()



