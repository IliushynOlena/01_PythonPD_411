'''
print ("Hello world")
print ("Hello world")
print ("Hello world")
print ("Hello world")
print ("Hello world")
print ("Hello world")
print ("Hello world")
print ("Hello world")
print ("Hello world")
print ("Hello world")

i = 0
while i < 10:
    i += 1# 1 2 3 4 5 6 7 8 9 10
    print (i , "Hello world")

# 1 - 10
i = 1

while i <= 10:
    print(i, )
    i+= 1

print()
# 10 - 1
i = 10 
while i >= 1:
    print(i, end=" ")
    i -= 1


print()

number = int(input("Enter number : ")) # 25
if number < 0 or number > 10:
    print("error")
else:
    i = 1
    while i <= 10:
        print(f"{number} * {i} = {number*i}")
        i += 1
    else:
        print("="*30)


# 12  - 35
i = 12
suma = 0
while i <= 35:
    print(i, )
    i+= 1

#1 - 15

#20 - 5
'''
#Користувач вводить із клавіатури два числа. Потрібно показати всі числа у вказаному діапазоні.

start = int(input("Enter start : "))#2
end = int(input("Enter end : "))#15

i = start
while i <= end:
    print(i, end=" ")
    i+=1

start = int(input("Enter start : "))#2
end = int(input("Enter end : "))#15

while start <= end:
    print(start, end=" ")
    start+=1