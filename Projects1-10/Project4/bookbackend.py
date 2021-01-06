import sqlite3

def connect():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book(id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
    conn.commit()
    conn.close()

def insert(title, author, year, isbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO book VALUES(NULL,?,?,?,?)",(title,author,year,isbn))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    conn.close()
    return rows

def search(title="", author="", year="", isbn=""): #Empty strings, annars kräven funktionen alltid 4 parametrar fastän användaren endast söker efter en enda
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book WHERE title = ? OR author = ? OR year = ? OR isbn = ?", (title, author, year, isbn))
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE id =?",(id,))
    conn.commit()
    conn.close()

def update(id, title, author, year, isbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("UPDATE book SET title = ?, author = ?, year = ?, isbn = ? WHERE id = ?",(title, author, year, isbn, id))
    conn.commit()
    conn.close()


connect()

# insert("Aladdin", "John Mccain", 1999, 929292929)
# insert("Calles book", "Calle Unnérus", 2009, 9293838929)
# delete(1)
# update(9, "Ny bok", "Inte Calle", 1929, 20203848)

# print(view())
# print(search(author = "Calle Unnérus"))