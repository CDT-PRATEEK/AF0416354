print("Line 1")
print("Line 2")
print("Line 3")
print("Line 4")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter Second number: "))

try:
    print(num1/num2)
    open("Anudip.txt")
    print("This is try block")

except (ZeroDivisionError, FileNotFoundError):     # to print seperate msg for each exception
    print("Something went wrong")                  # use multiple except blocks


print("Line 5")
print("Line 6")
print("Line 7")

