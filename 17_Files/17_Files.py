
# phone = "380956895454"
# print(phone)

# #відкрити файл
# #читати файл
# #записати файл
# #закрити файл
# #абсолютний шлях до файлу (повний шлях)
# url = r"C:\Users\helen\Desktop\NewGroups\01_PythonPD_411\17_Files\file_test.txt"
# #відносний шлях дo файлу (відносний шлях - відносно корінної папки, в якій відкритий VS code)
# file = open('./17_Files/file_test.txt')
# #file.read() - читає всю інформацію з файлу від початку до кінця
# #print(file.read())

# #file.readline() - читає інформацію  до переходу на новий рядок
# #print(file.readline().strip())

# #file.readlines() - читає всю інформацію з файлу від початку до кінця і повертає список рядків
# #print(file.readlines())

# #file.read(5) - читає інформацію згідно розміру вказаного в дужках
# print(file.read(15))

# file.close()

# #open()
# with open(url) as file:
#     line = file.read()
#     print(line)
#     print(type(line))

#     #file.close()

# # #режим перезапису файлу
# # url = './17_Files/write_file.txt'

# # with open(url,'w') as file:
# #     file.write("Lorem ipsum")

# #режим дозапису файлу
# lines = [
#     'Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
#     'Donec ac nunc convallis, sollicitudin tellus accumsan, dignissim augue.',
#     'In eleifend nisi eget ligula viverra, non posuere erat pharetra.',
#     'Nulla vitae justo finibus, pretium nisl et, laoreet dui.'
# ]
# url = './17_Files/write_file.txt'

# counter = 1
# with open(url,'a') as file:
#     for line in lines:
#         file.write(f"{counter}.{line}\n")
#         counter+=1
# #записуємо до файлу одразу весь список (ітерейбл колекшен )
# url = './17_Files/write_lines.txt'
# with open(url,'w') as file:
#     file.writelines(lines)

# def readFile(url):
#     with open(url,'r') as file:
#         return file.read()
    
# def appFile(url, info):
#     with open(url,'a') as file:
#         file.write(info)

# read_url = './17_Files/write_file.txt'
# write_url = './17_Files/write_lines.txt'

# text = readFile(read_url)
# appFile(write_url,text)
write_url = './17_Files/write_lines.txt'
lines = []
with open(write_url,'r') as file:
        lines = file.readlines()


with open(write_url,'w') as file:
        for line in lines[::-1]:
            file.write(line.strip()+'\n')
        print(file.readable())
        print(file.writable())

