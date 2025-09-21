num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1>num2:
    if num1>num3:
        print(num1, "is big")
    else:
        print(num3, "is big")
elif num2>num3:
    if num2>num1:
        print(num2, "is big")
    else:
        print(num1, "is big")
elif num3>num1:
    if num3>num2:
        print(num3, "is big")
    else:
        print(num2, "is big")

print(f"Numbers entered are {num1}, {num2}, {num3}")
print("End of program")