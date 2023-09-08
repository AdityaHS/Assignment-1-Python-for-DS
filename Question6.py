n = int(input("Enter number of students : "))
intial_tuple = ()

for i in range(n):
    a = str(input(f"Enter email id of {i+1} student : "))
    intial_tuple += (a,)
print(intial_tuple)


c = list(intial_tuple)
username_tuple = ()
domain_tuple = ()
for i in c:
    d = i.split("@")
    username_tuple += (d[0],)
    domain_tuple += (d[1],)

print(username_tuple, domain_tuple, sep = "\n")