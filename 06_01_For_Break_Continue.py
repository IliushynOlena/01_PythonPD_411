'''
line = "Hello world"# str
print(line)
print(line[0])
print(line[1])
print(line[2])
print(line[3])


i = 0
end = 10
while i <= end:
    print(line[i])
    i+= 1
print()

#some_string = input("Enter some line : ")
some_string = "Enter some line : "
for one_letter in  some_string:
    print(one_letter, end= "")
print("\n----------------------------------------")
for one_letter in  some_string[0:5:1]:
    print(one_letter, end= " ")
print("\n----------------------------------------")
for one_letter in  some_string[5:]:
    print(one_letter, end= " ")

print("\n----------------------------------------")
for one_letter in  some_string[2:7]:
    print(one_letter, end= " ")

print("\n----------------------------------------")
for one_letter in  some_string[::2]:
    print(one_letter, end= " ")

print()
for num in range(1,11):#start = 1, end = 10
    print(num, end=" ")
print()

for num in range(30):#start = 0, end = 29
    print(num, end=" ")
print()

for num in range(1,21,2):#start = 1, end = 20, step = 2
    print(num, end=" ")
print()

for num in range(1,21,3):#start = 1, end = 20, step = 3
    print(num, end=" ")
print()


while True:
    num = int(input(" 2 + 2 = ?  --> "))
    if num == 4:
        print("Congratulation!!!!!")
        break
    else:
        print("Enter number again : ")

print("Continue work......")
#break
#continue
i = 0
finish = int(input("Enter finish : "))
#0.......finish
while i < finish:
    # if i %3 != 0:
    #     print(i, end=" ")
    i +=1
    if i %3 == 0:       
        continue

    print(i, end=" ")
    
counter = 0
number = int(input("Enter number : "))#17  17/1 17/2 17/3 17/4 17/5 17/17
for i in range(1, number + 1 ):
    if number %i == 0:
        counter+=1
    
if counter > 2:
    print("Number is prime")
else:
    print("Simple")

    

flag = True#bool
number = int(input("Enter number : "))#17  17/1 17/2 17/3 17/4 17/5 17/17
for i in range(2, number//2 + 1 ):
    if number %i == 0:
        flag = False
        break
    
if not flag:#not = True-> False...False->True
    print("Number is prime")
else:
    print("Simple")
'''
name = "Olena teacher"# O l e n a
for s in name:
    print(s, end=" ")
print()
for s in name[:]:#start = 0 end = 4
    print(s, end=" ")
print()
for s in range(0,5):
    print(s, end=" - ")
    
    print(name[s], end=" ")
print()

for i in range(10):
    for j in range(10):
        print("*",end=" ")
    print()

for i in range(10):
    for j in range(10):
        if (i >= j):
            print("*",end=" ")
    print()