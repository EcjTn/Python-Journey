import random


while True:
    rev = random.randint(1,8)

    choices = int(input("Enter your guess number: "))


    if choices == rev:
        print("You won")
    else:
        print(f"Number rolled:  {rev}")
        print("You lose")