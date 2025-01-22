
#створення списку з використанням оператора []
category = ["Drama", "Comedy", "Fantasy"]

#створення списку з використанням конструктора класу list()
courses = list(("Python","HTML","C++","C#","SQL"))

print(category)
print(courses)


#створення пустого списку 
strudentMarks = []
students = list()
print(strudentMarks)
print(students)

#створення списку з вказанням елементів будь-якого типу даних
myList = ["Math",2365,5.13,"Yellow",True, False,[1,45,23,14]]
print(myList)

#створення списку з однотипними елементами
customers = ["Bob","Anna","Sophia","Jack","Bob","Jack"]
print(customers)

#створення списку, який складається з літер (ліст розділить слово на літери самостійно)
letters = list("Helloworld")
print(letters)

#створення списку з використанням генераторів
#newList = [expession for item in sequence]
#expession - вираз або формула для одного елементу
#for item in sequence - цикл, який дає нам послідовність елементів(або кількість ітерацій)
list_1 = [i*i  for i in range(6)]#for i in range(6)
print(list_1)
# #start = 0, end = 6, step = 1
# for i in range(6): #0 1 2 3 4 5 
#     print(i)

#генеруємо в список набір рандомних елементів
import random
random_numbers = [ random.randint(20,50)  for i in range(10)]
print(random_numbers)

#виводимо всі елементи списку за допомогою циклу
for num in random_numbers:
    print(num, end="  ")
print()

#генеруємо в список букви
list_2 = [i+"*"  for i in "example"]#e x a m p l e
print(list_2)

list_3 = [i for i in "language"]
print(list_3)
#"_" - сепаратор - символ для об*єднання елементів
# .join(list_3) - обєднує всі елементи списку в одну стрінгу
print("_".join(list_3))

line = "blue red green gray white black pink red green purple red green gray white black pink"
#split - ріже стрінгу по сепаратору, який вказаний у дужках
list_colors = line.split(' ')
print(list_colors)
for word in list_colors:
    print(word)
#при генерації елементів списку можна вказати умову, які саме елементи брати з послідовності
#пif condition  - умова
#newList = [expession for item in sequence if condition ]
#for i in range(1,11) # 1 2 3 4 5 6 7 8 9 10
list_4 = [i*i for i in range(1,11) if i%2== 0]
print(list_4)

list_4 = [i for i in range(1,11) if i%2== 0]
print(list_4)

#for i in range(1,11) # 1 2 3 4 5 6 7 8 9 10
list_4 = [i for i in range(1,11) if i%2== 1]
print(list_4)

#for i in range(1,11) # 1 2 3 4 5 6 7 8 9 10
list_4 = [i for i in range(1,11) if i > 0]
print(list_4)

#for i in range(1,11) # 1 2 3 4 5 6 7 8 9 10
list_4 = [i for i in range(1,11) if i < 0]
print(list_4)

customers = ["Bob","Anna","Sophia","Jack","Bob","Jack"]
#for i in customers = "Bob","Anna","Sophia","Jack","Bob","Jack"
list_5 = [name   for name in customers if name!= "Bob" and name != "Jack"]
print(list_5)
#for x in range(1,4) = 1 2 3 
#for y in range(1,4) = 2 3 4
#x= 1  1*2  1*3 1*4 
#x = 2 2*2 2*3 2*4
#x = 3 3*2 3*3 3*4
# for i in range(1,4):
#     for j in range(2,5):
#         print(i*j)

#     

list_6 = [x*y  for x in range(1,4)  for y in range(2,5)]
print(list_6)

list_7 = [[x*y  for x in range(1,4)]  for y in range(2,5)]
print(list_7)

myList = ["Math",2365,5.13,"Yellow",True, False,[1,45,23,14]]
print(myList)
print(myList[0])
print(myList[2])
print(myList[len(myList)-1])
print(myList[-1])
#зріз = [start : stop : step]
print(myList[1:3])
print(myList[-4:-2])
print(myList[1:-1])
#reverse 
print(myList[::-1])
print(myList[4::-1])
print(myList[-4::-1])

category = ["Drama", "Comedy", "Fantasy","Cartoon","Horor","History","Science"]
print(category)
category[0] = "Action"
print(category)
category[::2] = ["New name1","New name2","New name2","New name2"]
print(category)

userLogs = ["admin","student","teacher","hr","user"]
prices = [100,200,30,400,50]
print(len(userLogs))
print(len(prices))

print(sorted(userLogs))
print(sorted(prices))

print(min(userLogs))
print(min(prices))

print(max(userLogs))
print(max(prices))

#print(sum(userLogs)) #error
print(sum(prices))

#operator + 
category1 = ["Drama", "Comedy", "Fantasy"]
category2 = ["Cartoon","Horor","History","Science"]
print(category1+ category2)
print(category1*2)

for film in category1:
    print(film)

for index in range(len(category1)):
    print(category1[index])
print("Methods list : ")
print(category1)
#add new element in the end
category1.append("Fantasy")
print(category1)

#add range of elements in the end
category1.extend(category2)
print(category1)

#insert - add new element on the index
category1.insert(1,"Novel")
print(category1)

#remove - delete first element on value
category1.remove("Fantasy")
print(category1)

#pop - delete element on the index
category1.pop(0)
print(category1)


#pop - delete last element 
category1.pop()
print(category1)

#delete all element
category1.clear()
print(category1)

category1 = ["Drama", "Comedy", "Comedy","Comedy","Fantasy"]
#find element 
print(category1.index("Comedy"))
#print(category1.index("Comedyyyy"))

print(category1.count("Comedy"))

category1.sort()
print(category1)
#or 
category1.sort(reverse=False)
print(category1)

category1.sort(reverse=True)
print(category1)


customers = ["Bob","Anna","Sophia","Jack","Bob","Jack"]
print( "Bob" in customers)
print( "Olena" in customers)
if "Bob" in customers:
    print("Bob is customer")
else:
    print("Error")

numbers = [1,2,3,4,5]
# numbers_clone = numbers
# print(numbers)
# print(numbers_clone)

# numbers_clone[0] = 1000
# numbers_clone[1] = 55
# numbers_clone[-1] = 44

# print(numbers)
# print(numbers_clone)

#1 method copy
# numbers_clone_1 = numbers.copy()
# print(numbers)
# print(numbers_clone_1)
# numbers_clone_1[0]= 144
# print(numbers)
# print(numbers_clone_1)

#use list constructor
# numbers_clone_1 = list(numbers)
# print(numbers)
# print(numbers_clone_1)
# numbers_clone_1[0]= 144
# print(numbers)
# print(numbers_clone_1)

#3 user slice 
numbers_clone_1 = numbers[:]
print(numbers)
print(numbers_clone_1)
numbers_clone_1[0]= 144
print(numbers)
print(numbers_clone_1)

