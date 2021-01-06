#import necessities
import json
from difflib import SequenceMatcher
from difflib import get_close_matches


#read in json data
data = json.load(open("newdata.json"))

#create translate function
def translate (word):
    word = word.lower
    if word in data:
        return data[word]
    elif len(get_close_matches(data, word.keys())) > 0:
        guess = get_close_matches(data, word.keys())[0]
        q = input(guess + ": Y/N?")
        if q == "Y":
            return translate(guess)
        else: return "ok"
    else: "No such word"       


#continuously prompt user
while True:

    inp = input("Enter word: ")
    tra = translate(inp)
    if inp == "stop":
        break
    elif type(tra) == list:
        for el in tra:
            print(el)
    else:
        return translate(inp)

    

#Process output
