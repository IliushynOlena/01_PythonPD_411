
maxtrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(maxtrix)
print()
# get one row
for row in maxtrix:
    print(row)
print()
# get all elements 
for row in maxtrix:
    for elem in row:
        print(f"{elem} \t", end="")
    print()
print()
print(maxtrix[0])
print(maxtrix[0][0])
print(maxtrix[0][1])
print(maxtrix[0][2])
#get element by index
for i in range(len(maxtrix)):
    for j in range(len(maxtrix[i])):
        print(maxtrix[i][j], end=" ")
    print()

matrix_2 = [[j for j in range(7)] for i in range(6)]
print(matrix_2)

import random
maxtrix_random = []
row = 5
col = 6
# for i in range(row):
#     list = []
#     for j in range(col):
#         list.append(random.randint(10,40))

#     maxtrix_random.append(list)
for i in range(row):    

    maxtrix_random.append([random.randint(10,40) for j in range(col)])

for line in maxtrix_random:
    print(line)
print("-------------------------------------")
# list = 10 12 13 15 16 25
# for j in range(col):
#     print(random.randint(10,40),end=" ")
# print("-------------------------------------")
# print([random.randint(10,40) for j in range(col)])
# summa = sum(maxtrix_random)
# print(f"Summa = {summa}")
summa = 0
for row in maxtrix_random:
    summa += sum(row)
    print(f"Summa in row {sum(row)}")

print(f"Summa in matrix {summa}")

#summa elements in column
sum_column = 0
row = 5
for i in range(col):
    for j in range(row):
        sum_column+= maxtrix_random[j][i]
    print(f"Summa elements in column {sum_column}")

