print("Hello")
print("Hello","red")
print("Hello","red",5)
print("Hello","red",5,100)
print("Hello","red",5,100,3.26)
print("Hello","red",5,100,3.26,1.47)

#--------------------------1----------------
# def summaAllElements(a,b):
#     return a+b

# res= summaAllElements(5,7,8,9)
# print( f"Result = {res}")
#-------------2---------------------
#(5, 7, 8, 9, 14, 87) - cortege - don*t change 
#cortege - not allow add element, delete element, change element
def summaAllElements(*args):
    #change element - error - not allow
    #args[0]=1000
    #print(args) - print all elements
    #get all element one by one
    for elem in args:
        print(elem, end=" ")
    print()
    #get elemnt by index
    print(f"Element in index [4] = {args[4]}")
    #count element in cortege by value 
    print(f"Count element [5] = {args.count(5)}")
    print(f"Lenght element : {len(args)}")

    #how to change cortege --> create list
    my_list = list(args)
    print(my_list)
    return sum(args)


res= summaAllElements(5,12,5,48,96,5,78,36,5,47)
print( f"Result = {res}")

def showInfoByStudent(name, age, *marks):
    print(f"Name :{name}")
    print(f"Age :{age}")
    print(f"Marks :{marks}")

showInfoByStudent("Olga",17,12,12,11,10,9,12)

#lambda functions
def sum(a,b):
    return a+b

def show(color):
    print(color)

print(sum(5,14))
show("red")


lambda_show = lambda a,b:a+b
lambda_color =lambda color:print(color)
    
print(lambda_show(4,4))
lambda_color("white")

#1
numbers = [1,7,58,6,3,41,12,25,85,9]

def changeList(list):
    temp=[]
    for elem in list:
        temp.append(elem*2)
    return temp

print(numbers)
new_numbers = changeList(numbers)
print(new_numbers)

# #2_1
# line = input("Enter numbers : ").split(" ")
# line = [int(i) for i in line]
# print(line)
#2_2 - using lambda function
# line = list(map(int, input("Enter numbers : ").split(" ")))
# print(line)

# #exapmle 1 - map - change all elements 
# def double(x):
#     return x*2

# numbers = [1,7,58,6,3,41,12,25,85,9]
# change_numbers =  list(map(double,numbers))
# print(numbers)
# print(change_numbers)

# example 2 - map - change all elements - using lambda functions
numbers = [1,7,58,6,3,41,12,25,85,9]
change_numbers =  list(map(lambda x:x*2,numbers))
change_numbers_pow =  list(map(lambda x:x*x,numbers))
print(numbers)
print(change_numbers)
print(change_numbers_pow)

#Filter -- create new collection using some filter
numbers = [1,7,58,6,3,41,12,25,85,9,14,7,8,9,6,5,4,23]
even_numbers = list(filter(lambda x:x%2==0, numbers))
print(numbers)
print(even_numbers)

diapazon_numbers = list(filter(lambda x:x>0 and x < 10, numbers))
print(numbers)
print(diapazon_numbers)

colors = ["red", "green","blue","yellow","pink","grey"]

# def checkColor(color):
#     if len(color)> 4:
#         return True
#     else:
#         return False
    
# def checkColor(color):
#     return len(color)> 4

# print( 5 > 4)
# print( 10 > 4)
# print( 3 > 4)
# print( 1 > 4)
    
# print(colors)
# new_colors = list(filter(checkColor,colors))
# print(new_colors)

#using lambda function    
print(colors)
new_colors = list(filter(lambda color:len(color)> 4  ,colors))
print(new_colors)

new_colors = list(filter(lambda color:color[0]=='g'  ,colors))
print(new_colors)