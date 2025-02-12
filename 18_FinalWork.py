import json

def createOneUser():
    id = int(input("Enter id : "))
    name = input("Enter name : ")
    user = {'id':id,'name':name}
    return user

def createList(number):#number = 4
    users = []
    for i in range(number):
        users.append(createOneUser())
    return users

def writeUsersToFile(users):
    with open("users.json",'w') as file:
        file.write(json.dumps(users))

def readUsersFromFile():
    with open("users.json") as file:
        return json.loads(file.read())
    
def printAllUser(users):
    for i in range(len(users)):
        print(i+1, users[i])
# users = []
# users.append(fillUser())
while True:
    choice = int(input('''
                1 - Fill database 
                2 - Add new User
                3 - Delete user
                4 - Print user
                5 - Sort users
                0 - Exit
            '''))
    if choice == 1:
        number = int(input("Enter number of users : "))
        users = createList(number)
        writeUsersToFile(users)
    if choice == 0:
        print("Bye bye !!!")
        break
    if choice == 2:
        users = readUsersFromFile()
        #print(users)
        users.append(createOneUser())
        writeUsersToFile(users)
    if choice == 4:
        users = readUsersFromFile()
        printAllUser(users)
    if choice == 5:
        print("-------------Before sort-----------------")
        users = readUsersFromFile()
        printAllUser(users)
        print("-------------After sort-----------------")
        users.sort(key = lambda x:x['id'])
        printAllUser(users)





