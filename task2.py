'''Task 2: Design a simple calculator with basic arithmetic operations. 
Prompt the user to input two numbers and an operation choice.
Perform the calculation and display the result.'''


a=int(input("Enter the a number:-"))
b=int(input("Enter the b number:-"))
op=input("Enter the operator:-")

if op=='+':
    print("Addition of a and b is:-",a+b)
elif op=='-':
    print("Subtraction of a and b is:-",a-b)
elif op=='*':
    print("Multiplication of a and b is:-",a*b)
elif op=='/':
    print("Division of a and b is:-",a/b)
else:
    print("Invalid operator")
