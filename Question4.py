list1 = [25, 45, 85, 98, 43, 77]

while True:
    
    print("Do you want to insert or delete an element ? \nEnter 1 for insertion and 2 for deletion and 3 to exit.")
    ch = int(input())
    
    if ch == 1 :
        a = int(input("Enter element to be inserted : "))
        pos = int(input("Enter position to insert : "))
        list1.insert(pos-1, a)
        print("Updated list is ", list1)
        
    if ch == 2 :
        print("Do you want to delete element by value or by position or slice the list? \nEnter 1 or 2 or 3 accordingly")
        ch1 = int(input())
        
        if ch1 == 1:
            dlt = int(input("Enter element to be deleted : "))
            if dlt not in list1 :
                print("Entered element not found in list ")
            else :
                for i in list1 :
                    if i == dlt :
                        list1.remove(i)
        
        if ch1 == 2 :
            dlt = int(input("Enter position of element to be deleted : "))
            
            if dlt > len(list1) :
                print("Out of range !!")
            else :
                list1.remove(list1[dlt-1])
            
        if ch1 == 3 : 
            a = int(input("Enter start : "))
            b = int(input("Enter stop : "))
            c = int(input("Enter step : "))
            
            for i in range(a, b, c):
                list1.remove(list1[i])
        print("Updated list is ", list1)


    if ch == 3 :
        print("Exit")
        break
        