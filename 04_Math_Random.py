
a = 10
b = 12
c = 33
# Варіанти гарного форматування для виведення інформації
print(a,b,c)
print("a =", a,".", "b =", b,"." ,"c =", c, ".")
print("Numbers : a = {}. b = {}. c = {}.".format(a,b,c))
print("Numbers : a = {}. b = {}. c = {}.".format(b,a,c))
print("Numbers : a = {}. b = {}. c = {}.".format(c,a,b))
print(f"Numbers : a = {a}. b = {b}. c = {c}.")
#comment one line - однорядкові коментарі

'''
comment multyline - багаторядкові коментарі
'''
#Вірні варіанти називання змінних
# myVariable
# ageOfHuman
# age_of_human
print(a)
if a == 10:
    #algorithm
    pass# використовується, щоб вказати, що поки що немає ніякого алгоритму


print(a)
# print("Happy Hew Year')
# print("Happy Hew Year")
# print('Happy Hew Year')
# print('Happy Hew Year'

a = "Happy"
b = "New Year"
c = 2025
print(a+b)
#print(a+b+c)# не можна додавати два різних типи даних

a = 8 # ініціалізація
b = 22 # присвоєння
a == 8 # порівняння

import math #модуль для виклику математичних функцій

print(math.ceil(2.5))# заокруглює до більшого
print(math.floor(2.5))# заокруглює до меншого
print(math.pow(2,4))# підносить до степеня
print(math.sqrt(64))# знаходить корінь квадратний

import random #модуль для генерації рандомного значення
number = 7
print(number)
print(random.random())#0.....1 радномне число в діопазоні від 0 до 1
print(random.random())
print(random.random())
print(random.random())
print(random.randint(0,1))# радномне число в діопазоні від 0 до 1
print(random.randint(10,100))# радномне число в діопазоні від 10 до 100
print(random.randint(10,20))# радномне число в діопазоні від 10 до 20


# 270m - 1 kg
# > 500g - 200 m  za 1 kg
price_1 = 270
price_2 = 200
gramm = int(input("Enter weight (gramm) : "))#3500 g
kg = gramm / 1000

print(f"Your weight of candies : {kg} kg")

if (kg < 0.5):
    total = kg *price_1
else:
    total = kg * price_2

print(f"Your total price is {total} grn")


day = int(input("Enter day number [1-7] : ")) #3

if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
else:
    print("Error number day...")

12321  

day = int(input("Enter day number [1-7] : ")) #7
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case _:
        print("Error number day...")







