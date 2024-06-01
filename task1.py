

class Calculator:
    def __init__(self, num1, operation, num2):
        self.num1 = num1
        self.operation = operation
        self.num2 = num2
    def Sum(self):
        return self.num1 + self.num2
    def Subtract(self):
        return self.num1 - self.num2
    def Multiplication(self):
        return self.num1 * self.num2
    def Division(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return 0

while True:
    num1= int(input("Enter the first "))
    operation = input("Enter (+, -, *, /): ")
    num2 = int(input("Enter the second"))




    calc = Calculator(num1, operation, num2)
    if operation == "+":
        result = calc.Sum()
    elif operation == "-":
        result = calc.Subtract()
    elif operation == "*":
        result = calc.Multiplication()
    elif operation == "/":
        result = calc.Division()
    else:
        result = "Error"
    print(f"{num1} {operation} {num2} = {result}")









































#import math

#class Calculator:
#    def fact(n):
#        if n < 0:
#            return None
#        return math.prod(range(1, n + 1))
#    def power(a, b):
#        return a ** b
#   def sqrt(n):
#        if n < 0:
#            return None
#        return math.sqrt(n)
#n = int(input())
#a = int(input())
#b = int(input())
#print(n, Calculator.fact(n))
#print(a,b, Calculator.power(a, b))
#print(n, Calculator.sqrt(n))
