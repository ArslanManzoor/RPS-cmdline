
# A rock paper scissors game versus the computer

from random import randint

"""
def best_of_three():
    win_count = 0

    for yeet in range(0, 3):
        win_count += best_of_one()
    if win_count >= 2:
        print ("YOU WIN THE BEST OF THREE")
    else: print("YOU LOSE THE BEST OF THREE")
"""


def best_of_one():
    player_decision = input("\nPlease enter either \"rock\", \"paper\" or \"scissors\": ")

    computer_decision = randint(0, 2)

    # 0 is rock
    # 1 is paper
    # 2 is scissors
    #print("\n(the random integer is " + str(computer_decision) + ")\n")

    if computer_decision   == 0:
        print("\nThe computer played \"rock\"")
    elif computer_decision == 1:
        print("\nThe computer played \"paper\"")
    else:
        print("\nThe computer played \"scissors\"")


    if player_decision == "rock":
        if computer_decision == 0:
            #TIE
            print("YOU TIED\n")
            return 0
        elif computer_decision == 1:
            #LOSE
            print("YOU LOSE\n")
            return -1
        else:
            #WIN
            print("YOU WIN\n")
            return 1
    elif player_decision == "paper":
        if computer_decision == 0:
            #WIN
            print("YOU WIN\n")
            return 1
        elif computer_decision == 1:
            #TIE
            print("YOU TIED\n")
            return 0
        else:
            #LOSE
            print("YOU LOSE\n")
            return -1
    if player_decision == "scissors":
        if computer_decision == 0:
            #LOSE
            print("YOU LOSE\n")
            return -1
        elif computer_decision == 1:
            #WIN
            print("YOU WIN\n")
            return 1
        else:
            #TIE
            print("YOU TIED\n")
            return 0

best_of_one()

#best_of_three()
