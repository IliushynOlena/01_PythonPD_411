
# a = input("Enter first number")
# b = input("Enter second number")
# c = input("Enter third number")

# print(a,b,c)
# result = a+b+c
# print(result*3)
# result = int( a+b+c)
# print(result*3)

#Користувач із клавіатури вводить чотиризначне число. 
# Необхідно перевернути число і відобразити результат. 
# Наприклад, якщо введено 4512, результат — 2154.
# number = int(input("Enter number : "))

# print(number)
# #1234 = / , //, %  
# a = number//1000
# print("a = ",a)
# b = number//100%10
# print("b = ",b)
# c= number//10%10
# print("c = ",c)
# d = number%10
# print("d = ",d) 
# print(d,c,b,a)
# print(str(d)+ str(c)+str(b)+str(a))

#15%4 = 3
#1. 15/4 = 3.2154
#2. 3 * 4= 12
#3. 15 -12 = 3
'''
#12%10 =2
# 12/10 = 1.2    10*1 = 10 12-10 = 2
login = "helen"
print(login)
login = "admin"


a ,b ,c = 1,2,3
print(a,b,c)
a = b = c = 5 # <------------------------
print(a,b,c)

print("1 == 1:", 1 == 1) #True         
print("1 == 2:", 1 == 2)  #False       
print("1 != 1:", 1 != 1)    #False     
print("1 != 2:", 1 != 2)   #True       
print("1 > 1:", 1 > 1)     #False      
print("1 > 2:", 1 > 2)      #False     
print("2 > 1:", 2 > 1)     #True      
print("1 < 1:", 1 < 1)     #False      
print("1 < 2:", 1 < 2)     #True      
print("2 < 1:", 2 < 1)     #False      
print("1 >= 1:", 1 >= 1)   #True      
print("1 >= 2:", 1 >= 2)   #False      
print("2 >= 1:", 2 >= 1)    #True     
print("1 <= 1:", 1 <= 1)   #True      
print("1 <= 2:", 1 <= 2)   #True      
print("2 <= 1:", 2 <= 1)   #False    

print(bool(""))
print(bool(0))
print(bool(0.0))
print(bool(None))
print(bool("It Step"))
print(bool(1))
print(bool(5))
print(bool(-56))

# and
competent = True
responsible = False
print(competent and  responsible)

#or 
competent = False
responsible = False
print(competent or  responsible)

#not
competent = False
print(not competent)

print("Hello")
print("Friend")
print("Res")

age = int(input("Enter age : ")) 

#if age >= 18 and age <= 125:
if 18<= age <= 125:
    print("Hello in my game!!!!")
else:
    print("You are too small. Goodbye!")
'''
'''
day = int(input("Enter day number [1-7] : ")) #7

if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")
else:
    print("Error number day...")

    '''
login = input("Enter your login : ")

if login == "admin":
    password = input("Enter password : ")
    if password == "admin":
        print("Welcome!!!")
    else:
        print("Error password")     
elif login == "exit":
    print("Goodbye!!!")
else:
    print("Error")

#number%2 == 0 - parne
#number%2 == 1 - ne parne