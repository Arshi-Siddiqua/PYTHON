Dict= {
    "name" : ["Arshi", "Alisha", "Aqsa"],
    "class" : "BSc. Engg in CSE",
    "marks" : [40,50,34],
    "cgpa" : [2.33,4.00,3.44]
}
print(Dict.keys()) #Prints all the keys in the dictionary

print(list(Dict.keys())) #Type casting the keys into a list

#print(Dict["name2"]) #Error cause no name2 in dict
print(Dict.get("name2")) #Returns none cause no name2 in dict(Prefarable)

Dict.update({"job": ["student"]}) #Add something new in dictionary
print(Dict)