list=[3,2,4,5,5,2,97]

list.append(200) #Adds 200 at the end of the list
print(list)

list.sort() #Sorts the list in ascending order 
print(list)

list.sort(reverse =True) #Sorts the list in descending order
print(list)

list.reverse() #Reverses the list
print(list)

# To insert something at a specific index
# list.insert(index, element)

list.insert(3, 13)
print(list)

list.remove(200) #Removes the given element
print(list)

list.pop(4)
print(list) #Removes the element at the given index
