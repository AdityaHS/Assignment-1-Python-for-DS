a = str(input("Enter a list of numbers as a string : "))
b = a.split()

for i in range(len(b)):
    min_index = i
    for j in range(i+1,len(b)):
        if b[min_index] > b[j]:
            min_index = j

    b[i],b[min_index] = b[min_index],b[i]
 
print(b) 