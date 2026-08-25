array1=[2,4,6,8,10]
array2=[1,3,5,7]
array3= []

i=0;
j=0;

while i < len(array1) and j < len(array2):
    if array1[i] < array2[j]:
        array3.append(array1[i])
        i += 1
    else:
        array3.append(array2[j])
        j += 1

while i < len(array1):
    array3.append(array1[i])
    i += 1
while j < len(array2):
    array3.append(array2[j])
    j += 1
print(array3)