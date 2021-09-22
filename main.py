a = float(input("Enter 1st number "))
b = float(input("Enter 2nd number "))
operator = input("Enter operator ")

from caculator.add import sumation
from caculator.substraction import sub
from caculator.multiplication import mul
from caculator.division import div
from caculator.factorial import fact

if operator == "+":
    print("The addition = ",sumation(a,b))
elif operator == "-":
    print("The substraction = ",sub(a,b))
elif operator == "*":
    print("The multiplication = ",mul(a,b))
elif operator == "/":
    print("The division = ",div(a,b))
elif operator == "!":
    print("The factorial of {} = {} ".format((a),fact(a)))
else:
    print("This is not an operator, please try again")

    #comment
    #another comment
    #last comment
