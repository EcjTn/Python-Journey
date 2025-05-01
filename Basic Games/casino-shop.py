import random
import os

userpc = os.getenv('COMPUTERNAME')

def shops(money):
    while True:
        print(f"Balance: ${money}")

        print("""
    
        0. Exit shop

        1. Teddy Bear      -  $450
        2. Panda Pillow    -  $900
        3. Couple Shirt    -  $500
        4. Toy Gun         -  $130
        5. Gamer's Cup     -  $980   
    
        """)

        shop_choice = int(input(f"{userpc}@shop~# "))
        os.system("cls")

        if shop_choice == 0:
            gamble(money)

        elif shop_choice == 1:
            if money < 450:
                print("Sorry you can't buy this item.")
            elif money >= 450:
                money = money - 450
                print("New Item Bought!: Teddy Bear")

        elif shop_choice == 2:
            if money < 900:
                print("Sorry you can't buy this item.")
            elif money >= 900:
                money = money - 900
                print("New Item Bought!: Panda Pillow")

        elif shop_choice == 3:
            if money < 500:
                print("Sorry you can't buy this item.")
            elif money >= 500:
                money = money - 500
                print("New Item Bought!: Couple Shirt")

        elif shop_choice == 4:
            if money < 130:
                print("Sorry you can't buy this item.")
            elif money >= 130:
                money = money - 130
                print("New Item Bought!: Toy Gun")

        elif shop_choice == 5:
            if money < 980:
                print("Sorry you can't buy this item.")
            elif money >= 980:
                money = money - 980
                print("New Item Bought!: Gamer's Cup")

def gamble(money):
    while True:
        print(f""" 
        
        Current money: ${money}
        
        0. Exit        
        1. Gamble
        2. Shop
        
        """)
        gamble_choice = int(input(f"{userpc}@gamble~# "))
        os.system("cls")
        
        if gamble_choice == 1:
            cons = random.randint(1, 3)
            if cons == 1:
                moneyshow = random.randint(1,120)
                money = money + moneyshow
                print(f"You won ${moneyshow}!")
            else:
                print("You lost")
        elif gamble_choice == 0:
            print("Bye bye...")
            exit()

        elif gamble_choice == 2:
            shops(money)
            break

if __name__ == "__main__":
    print("""
      
      1. Casino --> shop, gamble, etc

    """)
    main_choice = int(input("Enter Choice: "))
    os.system("cls")
    money = 0
    if main_choice == 1:
        gamble(money)