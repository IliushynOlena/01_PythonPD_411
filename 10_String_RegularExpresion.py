
str_1 = "123"
str_2 = "234"
str_3 = "Lorem 21 ipsum red"
import re

#re - . ^ $ * + ? {} [] () \ | 
#pattern - це шаблон елементу для пошуку і перевірки
#re.search(pattern, str) - шукає перше співпадіння
print('=========================== re.search(pattern, str)=====================')
print(f"\t{str_1} ----> \t {re.search('1',str_1)}")
print(f"\t{str_2} ----> \t {re.search('1',str_2)}")
print(f"\t{str_3} ----> \t {re.search('1',str_3)}")
print("----------------------------------------------------------------------")
print(f"\t{str_1} ----> \t {re.search('12',str_1)}")
print(f"\t{str_2} ----> \t {re.search('12',str_2)}")
print(f"\t{str_3} ----> \t {re.search('12',str_3)}")
print("----------------------------------------------------------------------")
print(f"\t{str_1} ----> \t {re.search('[12]',str_1)}")
print(f"\t{str_2} ----> \t {re.search('[12]',str_2)}")
print(f"\t{str_3} ----> \t {re.search('[12]',str_3)}")
print("----------------------------------------------------------------------")
print(f"\t{str_1} ----> \t {re.search('[0-9]',str_1)}")
print(f"\t{str_2} ----> \t {re.search('[0-9]',str_2)}")
print(f"\t{str_3} ----> \t {re.search('[0-9]',str_3)}")

print("----------------------------------------------------------------------")
print(f"\t{str_1} ----> \t {re.search('[a-z]',str_1)}")
print(f"\t{str_2} ----> \t {re.search('[a-z]',str_2)}")
print(f"\t{str_3} ----> \t {re.search('[a-z]',str_3)}")
#True = 1   False = 0
print(bool("")) #False
print(bool(0))  #False
print(bool(0.0))#False
print(bool(None))#False
print(bool("It Step")) #True
print(bool(1))#True
print(bool(5))#True
print(bool(-56))#True
# #Example 1  - one small letter
# msg = input("Enter one letter : ")
# match = re.search('[a-z]', msg)

# if match:
#     print("This is letter ")
# else:
#     print("It is not letter ")
# #Example 1  - one small letter or big letter
# msg = input("Enter one letter : ")

# match = re.search('[a-zA-Z]', msg)

# if match:
#     print("This is letter ")
# else:
#     print("It is not letter ")
#some numbers of elements 
print("----------------------------------------------------------------------")
print(f"\t{str_1} ----> \t {re.search('[a-zA-Z]{5}',str_1)}")
print(f"\t{str_2} ----> \t {re.search('[a-zA-Z]{5}',str_2)}")
print(f"\t{str_3} ----> \t {re.search('[a-zA-Z]{5}',str_3)}")
print("----------------------------------------------------------------------")
print(f"\t{str_1} ----> \t {re.search('[a-zA-Z]+',str_1)}")
print(f"\t{str_2} ----> \t {re.search('[a-zA-Z]+',str_2)}")
print(f"\t{str_3} ----> \t {re.search('[a-zA-Z]+',str_3)}")

print("----------------------------------------------------------------------")
print(f"\t{str_3} ----> \t {re.search('Lorem',str_3).group(0)}")


str_1 = "123"
str_2 = "234"
str_3 = "Lorem 21 ipsum red"
#шукає всі співпадіння в тексті з заданим шаблоном
print('=========================== re.findall(pattern, str)=====================')
print(f"\t{str_3} ----> \t {re.findall('\w+',str_3)}")
print(f"\t{str_3} ----> \t {re.findall('\w+',str_3)[0]}")
print(f"\t{str_3} ----> \t {re.findall('\w+',str_3)[1]}")
print(f"\t{str_3} ----> \t {re.findall('\w+',str_3)[2]}")
print(f"\t{str_3} ----> \t {re.findall('\w+',str_3)[3]}")
match = re.findall('\w+',str_3)

for elem in match:
    print(elem)

#шукає всі співпадіння в тексті з заданим шаблоном і дозволяє йоно змінити на нове
print('=========================== re.findall(pattern, str)=====================')
#print(f"\t{str_3} ----> \t {re.sub('\w+', "white",str_3)}")
print(f"\t{str_3} ----> \t {re.sub('\w{3}', "white",str_3)}")


    # СПЕЦ. СИМВОЛИ
    # \d - Визначає символи цифр. 
    # \D - Визначає любий символ, який не є цифрою. 
    # \w - Визначає любий символ цифри, букви або нижнє підкреслення. 
    # \W - Визначає любий символ, який не є цифрою, буквою або нижнім підкресленням.. 
    # \s - Визначає любий недрукований символ, включаючи пробіл. (таб і перехід на новий рядок)
    # \S - Визначає любий символ, крім символів табуляции, нового рядка и повернення каретки.
    # .  - Визначає любий символ крім символа нового рядка.  
    # \. - Визначає символ крапки.


    # КВАНТИФИКАТОРЫ
    # ^ - з початку рядка. 
    # $ - з кінця рядка. 
    # * - нуль і більше входжень підшаблону в сторці.  
    # + - одне і більше  входжень підшаблону в сторці.  
    # ? - нуль чи одне  входження підшаблону в сторці.    
pattern = "\+380\d{9}|\+38\(\d{3}\)\d{7}|\+38\(\d{3}\)\d{3}\-\d{2}\-\d{2}"
phone_number = input("Enter phone number : ")
#match = re.search(pattern, phone_number).group(0)
match = re.search(pattern, phone_number).group(0)
print(match)


        

