collection= set()
collection.add(1)
collection.add(2)
collection.add(3)
collection.add(4)
collection.add("Arshi") #Can add string
collection.add((1,2,3)) #Can pass tupple
#collection.add([1,2,3]) #This will give error as list
#We can add only immutable data types in set
#Immutable means fixed values 
#We can not use mutable data types like list, dict, sets in set

print(collection)
#collection.clear() #This will clear the set
#collection.remove(2) #This will give error if the element is not present

collection.discard(5) #This won't show error if the element is not present
print(collection)

collection.pop() #This will remove the first element from the set
print (collection)

set1={1,2,3}
set2={2,3,4,4,8,15}
set3= set1.union(set2)
print(set3)

set4= set1.intersection(set2)
print(set4)