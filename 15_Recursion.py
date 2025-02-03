
# #x = 5! = 1*2*3*4*5
# def factorial(x):
#     dob = 1
#     for i in range(1,x+1):
#         dob*=i
#     return dob
# # def factorial(x):
    
# #     for i in range(1,x+1):
# #         i*=i

# #     return i
# print(factorial(5))

# # def ModifyName(userName):
# #     newName1 = userName.upper()
# #     newName2 = userName.lower()
# #     return newName1, newName2 #(newName1,newName2)
# #     print("Hello")
# #     print("Hello")
# #     print("Hello")
# #     print("Hello")

# # name = input("Enter your name : ")
# # print(ModifyName(name))
# # users = list(ModifyName(name))
# # print(users)
# # nameUpper, nameLower = ModifyName(name)
# # print(f"Name upper : {nameUpper}")
# # print(f"Name lower : {nameLower}")


# def checkLog(userLog):
#     if userLog == "admin":
#         return userLog.upper()
#     elif userLog == 'user':
#         return userLog.lower()
#     else:
#         return "Wrong login!"
    
# print(checkLog("admin"))
# print(checkLog("user"))
# print(checkLog("student"))


# def summa(*args):
#     print(args)
#     print(sum(args))

# summa(1,5,6)
# summa(1,5,6,14,45)
# summa(1,5,6,14,45,4589,25)


# def myFunction(*args):
#     print(args)
#     s = 0
#     k = 0
#     for elem in args:
#         s += elem
#         k += 1
#     return s/k
# print(f"1+2+3 = {myFunction(1,2,3)}")
# print(f"1+2+3+4+5 = {myFunction(1,2,3,4,5)}")
# numbers = [1,2,3,4,5,6,7,8,9]
# print(f"[15,7,8,9,6,32,14,78,25] = {myFunction(*numbers)}")

#Recursion - функція, яка викликає сама себе
# def sayHello():
#     print("Hello")
#     sayHello()

# sayHello()

#x = 5
#for i in range(1,x+1) ---> 1 2 3 4 5
# def factorial(x):
#     dob = 1 #1
#     for i in range(1,x+1):
#         dob*=i #1 * 1 = 1. 1 *2 = 2. 2 * 3= 6. 6 * 4 = 24. 24 * 5 = 120
#     return dob
#5! --> 5 * 4!   4* 3!  3 * 2! 2*1! 1
def factorial(x): #x = 3
    # 5 * 4 * 3 * 2 * 1 
    if x == 0 or x == 1:
        return 1
    return x * factorial(x-1)

print(factorial(5))

word = "madam"
def isPalindrom(word):
    if len(word) == 0:
        return True
    if word[0] == word[-1]:
        return isPalindrom(word[1:-1])
    else: 
        return False
    


    
    # if word == word[::-1]:
    #     return True
    # else:
    #     return False

print(isPalindrom(word))

word = "madam"
# index of one element
word[-1]
# [:] - zriz  start = 0 ; end = -1 (len(word)) - copy
copy_of_word = word[:] #"madam"
copy_of_word = word[:-1] #"madam"
#[::] - start = 0; end = -1 (len(word)); step = 1
copy_of_word = word[::]#"madam"