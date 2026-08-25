Array= [10, 25, 30, 45, 50]
Target= 30 #targeted value

for i in range (len(Array)): #Go in every index of the array
    if Array[i] == Target: #Cheking if the current value is equal to the targeted value
        print("Element found at index {i}") #Printing the index of the targeted value
        break
else:
    print(-1) #If the targeted value is not found then it will print -1