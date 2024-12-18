# start = int(input("Enter first number : "))
# end = int(input("Enter end number : "))

# i = start
# summa = 0
# dob = 1
# while i <= end:
#     print(f"{i}", end=" ")
#     summa += i
#     dob*=i
#     #print(i, end=" ") # 1 + 2 + 3 + 4 + 5... 0*1*2*3*4*5
#     i+=1

# print(f"Summa = {summa}")
# print(f"Dob = {dob}")

# count_stars = int(input("Enter count stars : "))#20
# i = 0
# while i < count_stars:
#     print("*",end="")
#     i+=1

# count_symbols = int(input("Enter count of symbol : "))#20
# symbol = input("Enter symbol : ")
# i = 0
# while i < count_symbols:
#     print(symbol,end="")
#     i+=1


# start = int(input("Enter first number : "))#1
# end = int(input("Enter end number : "))#10

# i = start
# while i < end:
#     print(i,end=" ")
#     i+= 1
# print()
# #10...1
# i = end
# while i >= start:
#     print(i,end=" ")
#     i-= 1
# print()

# i = start
# count_five = 0
# while i <= end:
#     if i%7 == 0:
#         print(f"{i}", end=" ")
#     if i%5== 0:
#         count_five+=1
#         print(f"{i} krante 5 ")
#     i+=1

# print(f"count_five = {count_five}")
start = int(input("Enter first number : "))#1
end = int(input("Enter end number : "))#10

i = start
while i < end:
    if i%3 == 0 and i%5 == 0:
        print(f"Fizz Buzz {i}")
    elif i%3 == 0:
        print(f"Fizz {i}")
    elif i%5 == 0:
        print(f"Buzz {i}")
    
    else:
        print(i)
    i+= 1