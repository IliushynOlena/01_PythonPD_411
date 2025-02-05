


# for i in range(10):    
#     for j in range(10):
#         print(" *", end=" ")
#     print()
# print("Continue......")



# for i in range(1 ,11):    
#     for j in range(1,11):
#         print(f"{i} * {j} = {i*j}")
#     print()
#     print()

floor = 1
energy = 70
print(f"I am on the {floor} floor")
while floor != 5:
    step = 0
    if floor == 3:
        print("I will take elevator")
        break
    while step != 20:
        step +=1
        energy -=1
        if energy == 0:
            print("I am tired. I will rest a little...")
            energy += 70

    floor+=1
    print(f"I am on the {floor} floor")

print("I am on the five floor")

x = 1
while x < 10:
    print(x, end=" ")
    x+=1
    break


print("Hello")
print("Hello")
print("Hello")
print("Test")

