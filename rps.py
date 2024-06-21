import random
import os
import time
rocklst = ['R','r','ROCK','rock']
paperlst = ['P','p','PAPER','paper']
scissorslst = ['S','s','SCISSORS','scissors']
ranlst = ['r','p','s']
score = 0
def win():
    print("win")
    score+=1
def tie():print("tie")
def loss():
    print("loss")
    score-=1
while True:
    os.system('clear')
    ranchoice = random.choice(ranlst)
    if score <= 0:score = 0
    print(f'score: {score}')
    choice = input('rock, paper, scissors [r/p/s] >> ')
    if choice == 'r':
        if ranchoice == 'r':tie()
        elif ranchoice == 'p':loss()
        else:win()
    elif choice == 'p':
        if ranchoice == 'r':win()
        elif ranchoice =='p':tie()
        else:loss()
    elif choice == 's':
        if ranchoice == 'r':loss()
        elif ranchoice == 'p':win()
        else:tie()
    elif choice == 'e':exit()
    else:print("invalid")
    time.sleep(1)
