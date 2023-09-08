a = int(input("Enter a number : "))
b = []


while a>1 :
    if a%2 == 0 :
        b.append("0")
    else :
        b.append("1")
    a = a/2
    continue


if a == 1:
    b.append("1")
if a== 0 :
    b.append("0")


print("".join(b[::-1]))