import random

comp_number = random.randint(1,500)
#print(f"Number {comp_number}")

count = 0
while True:
    user_number = int(input("Enter number [1-500] : "))
    count +=1

    if comp_number == user_number:
        print("You gess my number! You are winner!!!")
        print(f"Number = {comp_number}. Count attempts : {count}")
        break
    if user_number > comp_number  :
        print("Comp number is less")
    
    if user_number < comp_number:
        print("Comp number is bigger")

    
