#lists
numbers= [1,2,3,5]
words = ['red','green','blue']
some_list = [14,45,'green',True]
#cortege
cortege = (1,5,8)
cortege2 = ('red','green','blue')
cortege3 = (14,45,'green',True)

#dictionary 
#studentList = ['Stas','Bondar',17,11.8,'PD411','21.02.2007']
student = {
    #key:value
    #key - string, numbers
    'name':'Stas',
    'lastname':'Bondar',
    'age':17,
    'rating':11.8,
    'group':'PD411',
    'birthday':'21.02.2007'
}

print(student)
print(student['name'])
print(student['lastname'])
print(f"Name : {student['name']}. Lastname : {student['lastname']}")
#student.keys() - отримуємо всі ключі з словника 
#student[key] - отримання значення по певному ключу
for key in student.keys():
    print(f"Key : {key} ---> value: {student[key]}")

for key in student.keys():
    print(f" {key} {student[key]}")

#отримуємо всі значення з словника
for value in student.values():
    print(value,end=" ")
print("\n-----------------------------------------")
#отримуємо всі ключі and всі значення з словника
for key,value in student.items():
    print(f" {key} : {value}")

print(student.keys())
print(student.values())
print(student.items())

for item in student.items():
    print(f" {item[0]} ---> {item[1]} ")

print("----------Change object---------------------")
print(student)
#delete key and value 
del student['rating']
print(student)
#delete last element
student.popitem()
print(student)
#delete element by key
student.pop("lastname")
print(student)
#add new key and value 
student['email']="stas@gmail.com"
print(student)
# student['email']="helen@gmail.com"
# print(student)


list_student = [   
    {'name':'Stas1','lastname':'Bondar','age':17,'rating':11.8,'group':'PD411','birthday':'21.02.2007'},
    {'name':'Stas2','lastname':'Bondar','age':17,'rating':11.8,'group':'PD411','birthday':'21.02.2007'},
    {'name':'Stas3','lastname':'Bondar','age':17,'rating':11.8,'group':'PD411','birthday':'21.02.2007'},
    {'name':'Stas4','lastname':'Bondar','age':17,'rating':11.8,'group':'PD411','birthday':'21.02.2007'},
    {'name':'Stas5','lastname':'Bondar','age':17,'rating': 8,'group':'PD411','birthday':'21.02.2007'},
    {'name':'Stas6','lastname':'Bondar','age':17,'rating':11.8,'group':'PD411','birthday':'21.02.2007'},
    {'name':'Stas7','lastname':'Bondar','age':17,'rating':6,'group':'PD411','birthday':'21.02.2007','marks':[11,11,8,9,6,3]}
]

print(list_student[4])
print(list_student[4]['rating'])
print(list_student[6]['marks'])
print(list_student[6]['marks'][-1])

print("Stas 7 marks : ")
for mark in list_student[6]['marks']:
    print(mark,end= " ")
print()


import json
write_obj =  {'name':'Stas1','lastname':'Bondar','age':17,'rating':11.8,'group':'PD411','birthday':'21.02.2007'}

print(type(write_obj))
print(write_obj)
# with open("student.txt",'w') as file:
#     file.write(str(write_obj))

byte_obj = json.dumps(write_obj)
print(type(byte_obj))
print(byte_obj)

with open("student.json",'w') as file:
    file.write(byte_obj)

read_obj = json.loads(byte_obj)
print(type(read_obj))
print(read_obj)

with open("student.json") as file:
    info = file.read()
    print(info)
    read_obj = json.loads(info)

    print(read_obj['name'])
