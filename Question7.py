#question 7

def alpha(str1):
    count = 0
    for i in str1:
        if i.isalpha() :
            count +=1
    return count


def digit(str1):
    count = 0
    for i in str1:
        if i.isdigit() :
            count +=1
    return count

def symbol(str1):
    count = 0
    for i in str1:
        if i.isalnum() == False :
            count +=1
    return count
    
    
def upper(str1):
    count = 0
    for i in str1:
        if i.isupper() :
            count +=1
    return count
    
def lower(str1):
    count = 0
    for i in str1:
        if i.islower() :
            count +=1
    return count
    

str1 = str(input("Enter a string : "))


print(f"Number of alphaets in string : {alpha(str1)}")
print(f"Number of digits in string : {digit(str1)}")
print(f"Number of symbols in string : {symbol(str1)}")
print(f"Number of uppercase alphabets in string : {upper(str1)}")
print(f"Number of lowercase alphaets in string : {lower(str1)}")
