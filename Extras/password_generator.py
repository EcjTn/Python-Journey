import random
import string


def pwd(minLen):

    letters = string.ascii_letters
    specials = string.punctuation
    numbers = string.digits

    chars = letters
    chars += numbers
    chars += specials



    pwd1 = ""

    for i in range(minLen):
        pwd1 += random.choice(chars)

    print("Saved as NewPasswords.txt")

    with open("NewPasswords.txt", "a") as f:
        f.write(f"[*] Password: {pwd1} \n")



if __name__ == '__main__':

    minLen = int(input("Enter Password Length: "))

    if minLen < 25:
        print("Minimum length must be 25")
        exit()

    pwd(minLen)