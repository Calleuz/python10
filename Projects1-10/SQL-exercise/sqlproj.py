#BROKEN


import pandas
import mysql.connector
from difflib import SequenceMatcher
from difflib import get_close_matches


con = mysql.connector.connect(
    user = "ardit700_student", 
    password = "ardit700_student",
    host = "108.167.140.122",
    database = "ardit700_pm1database" 
)
word = input("Enter a word: ")

cursor = con.cursor()
query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s'" % word) #Select all from dicitonary where expression is word
close = cursor.execute("SELECT * FROM Dictionary WHERE length(Expression)<30")
results = cursor.fetchall()



while True:
    if word == "stop":
        break
    else:
        word = input("Enter a word: ")


if results:
    for result in results:
        print(result[1])
elif len(get_close_matches(word, close)[0])>0:
    guess = get_close_matches(word, close)[0]
    ask_user = input(f"Did you mean {guess}? type: Y (yes) or N (no) ")
else: print("No word found")
        
