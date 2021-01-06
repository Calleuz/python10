mylist = {"fruit1": "Banana", "fruit2": "Mango", "fruit3": "Apple"}

# for key in mylist:
#     print(key)
#     print(mylist[key])

list0 = ["C", "A","L","L","E"]
list1 = [1,2,3,4,5]
list15 = [10,20,30,40,50]
newlist = []
for num in list1:
    holder = []
    holder += num

for anothernum in list15:
    holder += anothernum
    newlist += list(holder)
            


print(newlist)

list2 = dict(zip(list0,newlist))
print(list2)