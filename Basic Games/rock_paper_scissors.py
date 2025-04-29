import random
import time
import os




#3
def winDecide(computer, player, win, lose):


    #Computer Side
    if computer == "rock" and player == "scissors":
        print("----- Computer WON -----")
        print(f"Wins: {win}")
        lose += 1
        print(f"Losses: {lose}")


    elif computer == "scissors" and player == "paper":
        print("----- Computer WON -----")
        print(f"Wins: {win}")
        lose += 1
        print(f"Losses: {lose}")


    elif computer == "paper" and player == "rock":
        print("----- Computer WON -----")
        print(f"Wins: {win}")
        lose += 1
        print(f"Losses: {lose}")




    #Player Side
    elif player == "rock" and computer == "scissors":
        print("----- Player WON -----")
        win += 1
        print(f"Wins: {win}")
        print(f"Losses: {lose}")

    elif player == "scissors" and computer == "paper":
        print("----- Player WON -----")
        win += 1
        print(f"Wins: {win}")
        print(f"Losses: {lose}")




    elif player == "paper" and computer == "rock":
        print("----- Player WON -----")
        win += 1
        print(f"Wins: {win}")
        print(f"Losses: {lose}")



    #Draw Side
    elif player == "rock" and computer == "rock":
        print("----- TIE -----")
        print(f"Wins: {win}")
        print(f"Losses: {lose}")

    elif player == "scissors" and computer == "scissors":
        print("----- TIE -----")
        print(f"Wins: {win}")
        print(f"Losses: {lose}")

    elif player == "paper" and computer == "paper":
        print("----- TIE -----")
        print(f"Wins: {win}")
        print(f"Losses: {lose}")

    return win, lose







#2
def computer(player, win, lose):
    list = ["rock", "paper", "scissors"]
    if player not in list:
        print("Invalid Options!")
        exit()
    computer = random.choice(list)
    print(f"Computer: {computer}")
    print(f"Player typed: {player} ")
    return winDecide(computer, player, win, lose)



#1
def game():

    win = 0
    lose = 0
    while True:

        print("""
    
        Rock
        Paper
        Scissors

        """)
        player = input("Enter Your choice: ").lower()

        os.system("cls")
        win, lose = computer(player, win, lose)


if __name__ == "__main__":
    game()