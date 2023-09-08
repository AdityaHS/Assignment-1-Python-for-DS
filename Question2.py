n1 = int(input("Enter number of elements in list 1 : "))

list1 = []
for i in range(n1):
    a = int(input(f"Enter {i+1} number of list 1 :"))
    list1.append(a)
    
n2 = int(input("Enter number of elements in list 2 : "))

list2 = []
for i in range(n2):
    a = int(input(f"Enter {i+1} number of list 1 :"))
    list2.append(a)
    
print(list1 + list2)