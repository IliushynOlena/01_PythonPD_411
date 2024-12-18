import random
print("\t\tWelcome to my first Game")
print("\t\tRock Paper Scissors")

user = 0
bot = 0



while True:
    user_score = 0
    bot_score = 0
    for round in range(3):#start = 0 ,end = 2
        print(f"---------------------------- Round {round + 1} ----------------------------------------")
        while True:
            user = input("\t [r] - rock;\n\t [p] - paper;\n\t [s] - scissors\n\t Enter ypur choice : ")
            user = user.lower()
            if user == 'r' or user== 'p' or user == 's':
                break
            else:
                print("Error choice .....")

        bot =random.choice('rps')
        print("\t Bot \t User")
        print(f"\t [{bot}] \t [{user}]")

        if (user== 'r' and bot == 's') or (user == 'p' and bot == 'r') or (user == 's' and bot == 'p'):
            user_score +=1
        elif (bot== 'r' and user == 's') or (bot == 'p' and user == 'r') or (bot == 's' and user == 'p'):
            bot_score+=1

    if user_score > bot_score:
        print("\n\t=============== Congratulations !!! User is winner!!!=========")
    elif bot_score > user_score:
        print("\n\t=============== Sorry !!! Bot is winner!!!You lose =========")
    else:
        print("\n\t=============== Draw =========")
    
    while True:
        user = input("Do you want play again ? [y] - Yes. [n] - No --> ")
        user = user.lower()
        if user == 'y' or user == 'n':
            break
        else:
            print("Error. Enter true choose !!!")

    if user == 'n':
        print("Have a nice day !!!!! Goodbye!!!!")
        break