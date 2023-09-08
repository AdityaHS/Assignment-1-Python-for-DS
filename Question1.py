subject1 = float(input("Enter marks for subject 1: "))
subject2 = float(input("Enter marks for subject 2: "))
subject3 = float(input("Enter marks for subject 3: "))

average = (subject1 + subject2 + subject3) / 3

if average >= 40:
    result = "Pass"
else:
    result = "Fail"

print("Average marks:",average)
print("Result:",result)
