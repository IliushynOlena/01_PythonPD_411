
# print("Hello world")

# #        name   age  score
# student=['Bob', 19, 95]

# users=['admin', 'teacher', 'manager']
# # for u in users:
# #     if u == "manager":
# #         print(u)
# template="Name: {}; age: {}; scores: {}."
# while True:
#     print("1-print info")
#     print("2-mofify info")
#     print("3-exit")
#     userChoice=input("Select menu item: ")
#     if userChoice=="1":
#         user=input("Login:")
#         if user in users:
#             print("Current information:")
#             print(template.format(student[0],student[1], student[2]))
#     elif userChoice=="2":
#         if user in users:
#             print("Current information:")
#             print(template.format(student[0], student[1], student[2]))
#             userAnsw=input("Change this info:y-n?")
#             if userAnsw=="y":
#                 name=input("Input new name:")
#                 age=int(input("Input new age:"))
#                 scores=input("Input new scores:")
#                 student[0]=name
#                 student[1]=age
#                 student[2]=scores
#                 print(template.format(student[0],student[1], student[2]))
#     elif userChoice=="3":
#         print("Bye!")
#         break
#     else:
#         print("Error: wrong menu item!")




# help(print)
# help(len)
a = 5# global variable 
def showMessage():
    # print(a)
    #local variable 
    # b = 11
    # print(b)
    print("Hello")


showMessage()
showMessage()
showMessage()
showMessage()
# print(a)
# print(b)

def showGreetingByUser(name):   
    print(f"Hello, {name}")

showGreetingByUser("Denus")
showGreetingByUser("Anya")
showGreetingByUser("Dima")
showGreetingByUser("Vlad")
# name = input("Enter your name : ")
# showGreetingByUser(name)

def summa(a,b):
    print(a + b)

summa(5,7)
summa(2,1)
summa(3,7)

def sum(a,b):
    res = a+b
    return res

def sub(a,b):
    res = a-b
    return res

def multy(a,b):
    res = a*b
    return res

def div(a,b):
    if b==0:
        return#break == return
    return a/b

# r = sum(5,10)
# print(r)
# print(sum(5,5))
def calculate(a,b,op):
    if op == '+':
        return sum(a,b)
    if op == '-':
        return sub(a,b)
    if op == '*':
        return multy(a,b)
    if op == '/':
        return div(a,b)
    
res = calculate(5,7,'+')
print(f"Result = {res}")
res =calculate(5,7,'-')
print(f"Result = {res}")
res =calculate(5,7,'*')
print(f"Result = {res}")
res =calculate(5,7,'/')
print(f"Result = {res}")

def getOperation(line):
    if line.find('+') != -1:
        return '+'
    if line.find('-') != -1:
        return '-'
    if line.find('*') != -1:
        return '*'
    if line.find('/') != -1:
        return '/'



# user_input = input("Enter example (2+2) ---> ")
# op = getOperation(user_input)
# a = float(user_input.split(op)[0]) 
# b = float(user_input.split(op)[1])
# print(a)
# res =calculate(a,b,op)
# print(f"Result = {res}")


import random
#( count, min, max) - required arguments 
def fillList( count, min, max):
    # my_list = [random.randint(min,max+1)   for i in range(count)]
    # print(my_list)
    # return my_list
    return [random.randint(min,max+1)   for i in range(count)]


#( count = 10, min = 1, max = 20) - default parameters  
def fillList( count = 10, min = 1, max = 20):
    return [random.randint(min,max+1)   for i in range(count)]



numbers = []
numbers = fillList(10,1,50)
print(numbers)

numbers = fillList()
print(numbers)

numbers = fillList(30)
print(numbers)

numbers = fillList(5,5)
print(numbers)

numbers = fillList(7,8,15)
print(numbers)