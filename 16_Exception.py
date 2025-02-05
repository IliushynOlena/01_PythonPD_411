# # #4. Напишіть функцію, яка підраховує суму цифр числа. 
# # # Наприклад: число 1357, сума 1 + 3 + 5 + 7 = 16.


# # #4. Напишіть функцію, яка підраховує суму цифр числа. Наприклад: число 1357, сума 1 + 3 + 5 + 7 = 16.


# # def cumaNambers(number):
# #     a = number//1000 
# #     print("a = ",a)
# #     b = number//100%10 
# #     print("b = ",b)
# #     c= number//10%10 
# #     print("c = ",c)
# #     d = number%10 
# #     print("d = ",d) 
# #     print(a+b+c+d)

# # number = int(input("Enter number : "))
# # cumaNambers(number)

# # def summaRecirsion(number):
# #     #1234  -> 1234%10 = 4  1234/10 = 123.4 123*10 = 1230 1234-1230 = 4
# #     #1234//10 = 123
# #     #123%10 = 3
# #     #123//10 = 12
# #     #12%10 = 2
# #     #12//10 = 1
# #     #1%10 = 1
# #     #1//10 = 0
# #     #return 4 + 3 + 2 + 1 + 0
# #     if number == 0:
# #         return 0
# #     return number%10 + summaRecirsion(number//10)
 
# # print(summaRecirsion(number))
# number_1 = None
# number_2 = None

# while number_1 == None or number_2 == None:
#     try:
#         number_1 = int(input("Enter number : ")) 
#         number_2 = int(input("Enter number : ")) 
#         print(f"Number = {number_1/number_2}")
#         #print(f"Number = {number_1/number_2, num3}")
    
#     except ValueError:
#         print("Error type. You need enter number!")
#     except ZeroDivisionError:
#         print("You can*t divide by zero. Study math!!!")
#     except Exception:
#         print("Some unknown error")

# print("Continue......")
# print("Continue......")
# print("Continue......")

# #запускаємо код безумовно
# try:
#     age = int(input("Enter age : "))
#     if age < 0 :
#         #кидаємо помилку 
#         raise Exception("Age error. Age < 0...")
#     if age > 120:
#         #кидаємо помилку 
#         raise Exception("Age error. Age > 120")
    
        
# #ловимо помилку типу ValueError
# except ValueError:
#     print("Error type. You need enter number!")   
# #ловимо помилку типу Exception де exception - змінна, в яку ми піймали помилку з raise Exception("Age error. Age < 0...")
# except Exception as exception:
#     print(exception)
#     print(f"Type exception {type(exception).__name__} : {exception}")
# #відпрацює коли все буде добре і не буде згенеровано жодне виключення
# else:
#     print("It is ok!!!")
# finally:
#     #записати інформацію до файлу
#     print("Finally block")

colors = ['red','green','blue','pink','black',"white"]
try:
    index = int(input("Enter position of color : "))
    print(colors[index])
except ValueError:
    print("ValueError")
except IndexError:
    pass
    #print("Index incorrect")
print("Continue...")