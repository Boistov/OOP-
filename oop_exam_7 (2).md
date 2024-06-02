# EXAM FOR WEEK 6

## KEEP IN MIND: YOU ARE DOING THIS FOR YOUR BRIGHT FUTURE, SO GIVE YOUR 120%!
## ПОМНИТЕ: ВЫ ДЕЛАЕТЕ ЭТО ДЛЯ СВОЕГО СВЕТЛОГО БУДУЩЕГО, ПОЭТОМУ ВЫКЛАДЫВАЙТЕСЬ НА ВСЕ СВОИ 120%!

## RULES:
> No interner, no help to each other!

> Make one file and place all your work there (e.g. odina_kholiqov.py)

> Send the file at 

> You have 2 hours only

### 1 Question
What is OOP and why is it important? Write about main principles of OOP.
Чиро ООП мегуянд ва барои чӣ он лозим аст? Дар бораи принсипҳои асосии он нависед.
mo dorem dar oop inhoro ki har yakeashon yak vazifaro ijro mekunand 
1. Inheritance - merosiri kardan. meboshad and yak class metavonad meros girad misli padari va pisari 
2. Encapsulation - дохилии объектро тавассути маҳдуд кардани дастрасии мустақим ба маълумоти он муҳофизат мекунад. Он маълумот attribues ва methods ба як воҳид class муттаҳид мекунад.
3.Abstraction ба мо имкон медиҳад, ки тамаркуз ба хусусиятҳои муҳим ҳангоми пинҳон кардани ҷузъиёти нолозим

va baroi on OOp mashur hast va ziyod istifoda meshavad ki hvaqte ki mo kodi khudro navishtem va metavonem onro digaron nizz badi mo fahmand va dark kunand kodi mo dar borai chi hast va istifoda shudfa istodast 

OOp hamchun baronoma navisii sheygaroi istifoda mebarem va baroi mashhur budanash in ast ki kori moro oson va qulay mekunad 
va mo hachun barnoma soz agar bo in abzor kor kunem kodi khudamon baroi digaron  fahmotar meboshad va digar odam niz metavonad on kodro fahmad ki dar borai chi hast yo chi vazifaro istifoda mebarad 









### 2 Question
What are getter and setter and how to use them? Write about properties in python.
Getter ва setter чист ва чӣ тавр онҳоро истифода мебарем? Дар бораи хусусиятҳо(properties) дар python нависед.

Getter ва setter методҳо барои манобаи атрибутҳои классҳо дар Python истифода мешаванд Ин методҳо барои дастгирии атрибутҳои private ва таъмини encapsulation истифода мешаванд Mo метавонед атрибутҳоро бо хусусиятҳои функсионал дар классҳо истефода баред








### 3 Question
Types of variables and methods in a class.
Кадом намуди атрибутҳо ва методҳо дар клас мавҷуданд. 
dar class mo dore 
instace variable in variablho ba khudi object taaluq dorand 
class variable in variable ho boshand ba khudi class taaluq dorand va class boshad in naqsha mo objecta az rui class mesozem 

va 

instace methdod 
class method 


### 4 Question
Write about constructor and destructor.
Дар бораи конструктор ва деструктор нависед.

constructor in baroi sokhtani objecthoi class hast va istifoda meshavad va vaziifai asosish in sokhtani object meboshad baroi sokhtani objecti class __new __ lozim hast va istifoda meshavad .va __init__ baroi bakhashidani qimathoi doda shuda ba taghiryobandahoi dokhili class meboshand 

Constructor функсияи, ки автоматан пеш аз ин, ки обекти аз класс иҷоза шавад, иҷоза мешавад.
Destructor  функсияи, ки пеш аз таҳлили обекти класс, автоматан иҷоза мешава.


### 5 Question
Difference between global, local and nonlocal variables.
Фарқият байни тағйирёбандаҳои global, local and nonlocal.

забони Python, маълумотҳои муҳим дар бораи тағйирёбандаҳои global local  ва nonlocal мавҷуданд 

1. Глобал маълумотҳо дар барнома дар барои ҳама мақолаҳо ва функцияҳо мавҷуданд

2 Муҳитии махсус маълумотҳо дар ҳадди функцияҳо ва классҳо дароз карда мешаванд
3. Ин маълумотҳо аз муҳити барномаи берунӣ make outside of our program  омода мешаванд







### 1 
Create a program that asks the user for a range of numbers (x, y) and displays the multiplication tables from x to y.
Барномае созед ки аз консол 2 рақамро қабул мекунад. Барои ҳар як адади дар ин давр вуҷуддошта ҷадвали зарбашро нишон диҳад.
### EXAMPLE
# INPUT
    From = 2
    To = 3
# OUTPUT
    2x1= 2
    2x2= 4
    2x3= 6
    2x4= 8
    2x5= 10
    2x6= 12
    2x7= 14
    2x8= 16
    2x9= 18
    2x10= 20
    
    3x1= 3
    3x2= 6
    3x3= 9
    3x4= 12
    3x5= 15
    3x6= 18
    3x7= 21
    3x8= 24
    3x9= 27
    3x10= 30




ansver
class Karat:
    def karat_a_b(self):
        a, b = None, None
        while a is None or b is None:
            num1 = input()
            num2 = input()
            if num1.isdigit() and num2.isdigit():
                a, b = int(num1), int(num2)
            else:
                print("error")
        return a, b
    def karat(self, a, b):
        for num in range(a, b + 1):
            print(num)
            for i in range(1, 11):
                result = num * i
                print(f"{num} x {i} = {result}")
            print()
            
            
javob = Karat()
start, b = javob.karat_a_b()
javob.karat(start, b)







### 2
Create a class of Circle with instance variable like radius and class variable like PI(3.14). Then create a constructor which initializes the radius(radius comes as a parameter of constructor).
Your class should have the following methods:
Як класи Circle ки аз як тағйирёбандаи ба клас таалуқдошта PI = 3.14 ва як тағйирёбандаи ба обект тааллуқдошта radius ки қиммати он аз конструктор гузошта мешавад созед. Класи Шумо аз методҳои зерин бояд иборат бошад:

1. get_area();               // area = 2 * PI * R * R
2. get_diametr();           // diameter = 2 * R
3. get_circumference();      //  circumference  = 2 * PI * R
4. get_radius();             // radius  = R



                                          ansver:
class Qimat:
    def __init__(self, radius):
        self.radius = radius
    def get_area(self):
        return 2 * 3.14 * self.radius ** 2
    def get_diameter(self):
        return 2 * self.radius
    def get_circumference(self):
        return 2 * 3.14 * self.radius
    def get_radius(self):
        return self.radius

radius_value = float(input())
num = Qimat(radius_value)
print(num.get_area())
print(num.get_diameter())
print(num.get_circumference())
print(num.get_radius())








### 3
Create a Calculator class with this static methods:
Класи Калкуляторро бо методҳои статикии зерин созед:
1. factorial(n)
2. power(a, b)
3. sqrt(n)

import math

class Calculator:
    def factorial(n):
        if n < 0:
            return None
        return math.prod(range(1, n + 1))
    def power(a, b):
        return a ** b
    def sqrt(n):
        if n < 0:
            return None
        return math.sqrt(n)

n = int(input())
a = int(input())
b = int(input())
print(n, Calculator.factorial(n))
print(a,b, Calculator.power(a, b))
print(n, Calculator.sqrt(n))












### 4
Write a program in Python that asks the user for two numbers and one operation (+, -, *, /) then calculate the operation and display the result on the screen.
You should to follow this steps:
Як класи Calculator созед ки дар конструктор атрибутҳои зеринро дорост. Рақами якум, амал(+, -, *, /) ва рақами дуюм. Калкулятори Шумо баяд 4 амали математикиро иҷро кунад. Берун аз клас як даври беохир(infinite loop) созед. Объекти класи Калкуляторро созед ва рақамҳо ва аломати дохил кардаатонро ба он гузоред. math case - ро барои  даъват кардани методиҳои клас вобаста ба аломати дохилкарда истифода баред.

1.	Create class Calculator 
2.	Create a constructor which initializes the first number, operation(+, -, *, /) and second number(first num, second num, operation comes as parameter of constructor).
3.	Create four instance methods like: 
    Sum()
    Subtract()
    Multiplication()
    Division()
4.	Create infinite loop outside Calculator class 
5.	Use the math case block for calling methods
### EXAMPLE
# input 
    The first number is: 3
    The operation is: +
    The second number is: 1
# output
    3 + 1 = 4

    ????  
               


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












### 5 Question
Write an access control in PYTHON that asks the user for the username and password. Both must be integers from user.
You should to follow this steps:
1. Create a User class with attributes like First name, Last name, Username and Password. All atributes should init from constructor(__init__).
2. Create a UserManager class with this methods:
    register() -> in this method you should create object of User, input user information from console and append to list_of_users.
    
    login() -> this method should to check if user login and password both correct should print Login successful! or this user is not to list_of_user print User with this username not found and password incorrect print Password incorrect.
    
    change_password() -> this method for changing password by username, old_password and new_password
	
    GetUser() -> get all users from list_of_users

Як барнома созед ки вазифаҳои зеринро иҷро кунад. Регирстратсия, логин, ивази парол, истифодабарандагон.
Барои ҳалли ин масъала класи User бо атрибутҳои First name, Last name, Username ва Password созед. Ҳамаи атрибутҳо аз конструктор ворид карда шаванд. Класи дигар ки бояд созед ин UserManager ки аз методҳои register(), login(), change_password() ва GetUser() иборат аст.
    register() -> дар ин метод обекти класи User - ро созед маълумотҳояшро аз консол дохил карда онро ба листи  list_of_users дохил кунед. 

    login() -> дар ин метод бошад санҷед агар истифодабар бо ҳамин логир ва парол дар list_of_users бошад дар консол  Login successful! - ро нишон диҳед ва агар набошад User with this username not found, ё паролаш нодуруст бошад     Password incorrect!
    
    change_password() -> дар ин метод истифодабар метавонад бо дохил кардани username, old_password ва new_password паролашро иваз кунад.
	
    GetUser() -> ин метод бошад бо як формати хуб ҳамаи маълумотҳои истидабаронро дар консол нишон диҳад.






class User:
    def __init__(self, firstname, lastname, username, password):
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.password = password



class UserManager:
    def __init__(self):
        self.list_of_users = []
    def register(self):
        firstname = input()
        lastname = input()
        username = input()
        password = int(input())  
        user = User(firstname, lastname, username, password)
        self.list_of_users.append(user)
        print(username)
    def login(self):
        username = input("Username: ")
        password = int(input("passowrd") )
        found_user = next((user for user in self.list_users if user.username == username), None)
        if found_user:
            print("successful!")
        else:
            print(username)
            
            
            
    def change_password(self):
        username = input("Username: ")
        old_password = int(input("Enter Old Password"))
        new_password = int(input("Enter New Password"))
        found_user = next((user for user in self.list_of_users if user.username == username), None)
        if found_user:
            if found_user.password == old_password:
                found_user.password = new_password
                print("successfully!")
            else:
                print("incorrect.")
        else:
            print(f"User {username}' not found.")
            
         
    def GetUser(self):
        print("registered")
        for user in self.list_of_users:
            print(f"{user.first_name} {user.last_name} ({user.username})")


