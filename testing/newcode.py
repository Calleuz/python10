# myfile = open("fruits.txt")
# print(myfile.read())

# # with open("vegetables.txt", "w") as veg_file:
# #     veg_file.write("Cucumber\nTomato\nSalad")


# with open("vegetables.txt", "w") as veg_file:
#     veg_file.write(myfile.read())

# with open("bear.txt") as my_file:
#     new_file = my_file.read()
#     for el in new_file[:91]:
#         print(el)

# Single character and file and counts occurences of character in file

# def main (char, file):
#     open(file)
#     stringed = file.read()
#     return stringed.count(char)

# with open("bear.txt") as my_file:
#     new_file = my_file.read()[:90]
#     with open("first.txt", "w") as w_file:
#         for char1 in new_file:
#             for char in char1:
#                 w_file.write(char)


# import sys
# import time

# while True:
#     with open("first.txt") as file:
#         print(file.read())
#         time.sleep(3)
        
    
import sys
import os
import time
import pandas

while True:
    if os.path.exists("vegetables.txt"):
        with open("vegetables.txt") as file:
            print(file.read())
    else: print("File does not exist")
    time.sleep(3)
