import random
import os
import time
rocklst = ['R','r','ROCK','rock']
paperlst = ['P','p','PAPER','paper']
scissorslst = ['S','s','SCISSORS','scissors']
ranlst = ['r','p','s']
score = 0
while True:
    os.system('clear')
    ranchoice = random.choice(ranlst)
    if score <= 0:
        score = 0
    print(f'score: {score}')
    choice = input('rock, paper, scissors [r/p/s] >> ')
    if choice == 'r':
        if ranchoice == 'r':
            print("tie")
        elif ranchoice == 'p':
            print("loss")
            score -= 1
        else:
            print("win")
            score += 1
    elif choice == 'p':
        if ranchoice == 'r':
            print("win")
            score += 1
        elif ranchoice =='p':
            print("tie")
        else:
            print("loss")
            score -= 1
    elif choice == 's':
        if ranchoice == 'r':
            print('loss')
            score -= 1
        elif ranchoice == 'p':
            print("win")
            score += 1
        else:
            print('tie')
    elif choice == 'e':exit()
    else:print("invalid")
    time.sleep(1)
