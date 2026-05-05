"""TASK 1: BMI CALCULATOR """
weight = input("Enter your weight in kg: ")
height = input("Enter your height in m: ")
BMI = float(weight) / (float(height) ** 2)
if BMI < 18.5:
    print("You are underweight.")
elif BMI >= 18.5 and BMI < 25:
    print("You have a normal weight.")
else:
    print("You are overweight.")
print("Your BMI is: " + str(BMI))

""" TASK 2:CALCULATOR"""
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
operation = input("Enter the operation (+, -, *, /): ")
if operation == "+":
    result = float(num1) + float(num2)
elif operation == "-":
    result = float(num1) - float(num2)
elif operation == "*":
    result = float(num1) * float(num2)
elif operation == "/":
    result = float(num1) / float(num2)
print("The result is: " + str(result))
""" TASK 3: GUESS THE NUMBER """
numb1 = int(input("Enter a number between 1 and 10: "))
numb2 = int(input("Enter another number between 1 and 10: "))
numb3 = int(input("Enter a third number between 1 and 10: "))
 
check= numb1 == numb2 and numb1 == numb3 and numb2 == numb3
check2 = numb2 == numb1 or numb1 == numb3 or numb2 == numb3
max = max(numb1, numb2, numb3)
if check:
    print("gtxovt sheiyvanot gansxvavbeui ciprebi") 
elif check2:
     print("gtxovt sheiyvanot gansxvavbeui ciprebi")
     
else:
    print(max)