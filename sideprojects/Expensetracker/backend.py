import sqlite3

def connect():
    conn = sqlite3.connect("entries.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS cost(id INTEGER PRIMARY KEY, what text, nar text, cost float, who text)")
    conn.commit()
    conn.close()

def insert(what, nar, cost, who):
    conn = sqlite3.connect("entries.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO cost VALUES(NULL,?,?,?,?)",(what, nar, cost, who))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("entries.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM cost")
    rows = cur.fetchall()
    conn.close()
    return rows

def c_costs():
    conn = sqlite3.connect("entries.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM cost WHERE who = 'C' OR who = 'c'")
    rows = cur.fetchall()
    conn.close()
    return rows
def l_costs():
    conn = sqlite3.connect("entries.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM cost WHERE who = 'L' OR who = 'l'")
    rows = cur.fetchall()
    conn.close()
    return rows

def search(what="", nar="", cost="", who=""): #Empty strings, annars kräven funktionen alltid 4 parametrar fastän användaren endast söker efter en enda
    conn = sqlite3.connect("entries.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM cost WHERE what = ? OR nar = ? OR cost = ? OR who = ?", (what, nar, cost, who))
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect("entries.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM cost WHERE id =?",(id,))
    conn.commit()
    conn.close()

def update(id, what, nar, cost, who):
    conn = sqlite3.connect("entries.db")
    cur = conn.cursor()
    cur.execute("UPDATE cost SET what = ?, nar = ?, cost = ?, who = ? WHERE id = ?",(what, nar, cost, who, id))
    conn.commit()
    conn.close()

def delete_latest():
    conn = sqlite3.connect("entries.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM cost WHERE id = (SELECT MAX(id) FROM cost)")
    conn.commit()
    conn.close()


connect()
#insert("Mat", "10.12.2020", 393.9, "Calle")
#print(view())


