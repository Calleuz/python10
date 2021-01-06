import json
from difflib import SequenceMatcher
from difflib import get_close_matches

data = json.load(open("newdata.json"))

def translator (word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys()))>0:
        guess = get_close_matches(word, data.keys())[0]
        ask_user = input(f"Did you mean {guess}? type: Y (yes) or N (no) ")
        if ask_user == "Y":
            return translator(guess)
        else: 
            return "Okay, we thought it looked similar! "    
    else:
        return "There is no such word"

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


inp = input("Enter a word: ")
while True:
    if(inp == "stop"):
        break
    else:
        res = translator(inp)
        if type(res) == list:
            print("\n")
            for el in res:
                print(el)
            print("\n")
        else: 
            print("\n")
            print(res)
            print("\n")
        inp = input("Enter a word: ")


    


