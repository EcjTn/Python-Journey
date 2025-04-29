import socket
import os
import requests
import time
import random
from bs4 import BeautifulSoup
import base64




def check():
    while True:
        print(f"\nEX for Exit.")
        IP = input("Enter IP: ")
        if IP == "EX":
            print("Quitting...")
            break



        PORT = int(input("Enter Port: "))
        checker(IP, PORT)

        if checker(IP, PORT):
            print(f"[{IP}:{PORT}] is Online.")
        else:
            print(f"[{IP}:{PORT}] is Offline.")








###### UP and DOWN connected ######
def checker(IP, PORT):
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(3)
        client.connect((IP, PORT))
        client.close()
        return True
    except Exception as e:
        print(e)
        return False
    finally:
        print("Closing...")




def hostname():
    while True:
        print("\nEX for Exit.")
        hoster = input("Enter Hostname: ")
        if hoster == "EX":
            print("Quiting...")
            break
        new = socket.gethostbyname_ex(hoster)
        resultz = (f"{hoster} >>> {new}")
        print(resultz)

        str(resultz)

        with open ("hostnames.txt", "a") as f:
            f.write(f"{resultz} \n")
        
        fx = open('hostnames.txt')
        print(fx.read())





def reqz():

    type = input("Enter proxy type(socks4/http): ")
    url = f"https://api.proxyscrape.com/v2/?request=getproxies&protocol={type}&timeout=10000&country=all&ssl=all&anonymity=all"
    response = requests.get(url)
    print(f"REQUESTED URL: {url}")

    if response.status_code == 200:
        os.mkdir("ProxyList")
        print("Saved proxies to Proxylist/list.txt")
        with open("ProxyList/list.txt", "wb") as f:
            f.write(response.content)

    else:
        print("Error socks")


def htmler():
    while True:
        url = input("Enter URL: ")
        print("Saved HTML to HTML/url.html")
        os.mkdir("HTML")
        response = requests.get(url)

        with open("HTML/url.html", "w", encoding="utf-8") as f:
            f.write(response.text)





def scraper():

    todofol = input("Name your Folder: ")
    todolis = input("File name(for saving): ")



    try:
        os.mkdir(f"{todofol}")
    except Exception as e:
        print("That folder already exists, we will use that still.")
    finally:
        print("Finalizing...")






    letter = input("Enter your letter: ")

    with open(f"{todofol}/{todolis}.txt", "a") as ltr:
        ltr.write(f"{letter}\n")

    while True:
        
        letter = input("New letter(EX for exit): ")

        if letter == "EX":
            print("Quitting...")
            exit()

        with open(f"{todofol}/{todolis}.txt", "a") as ltr:
            ltr.write(f"{letter}\n")







def passbst():
    password = input("Enter Password: ")

    encoded_pass = base64.b64encode(password.encode())

    print(f"Password succesfully Encoded: {encoded_pass}")




def passdct():

    decoder = input("Enter what u want to decode: ")


    try:
        decoded_pass = base64.b64decode(decoder)
        decoded_data = decoded_pass.decode()
        print(f"Decoded Data: {decoded_data}")
    except Exception as en:
        print(en)



def timr():
    user = input("Click Enter to run: ")
    time.sleep(2)
    print("Executing...(1, 999)")
    time.sleep(3)

    zrandom = random.randint(1,89465)

    print(f"[*] First Random : {zrandom}")
    print("[*] Running randoms...")
    time.sleep(3)



    while True:

        chars = ['Carfulc', 'Personaficed', 'Etheum']
        crandom = random.choice(chars)

        verify = ['Key', 'Token', 'Encrypted']
        vrandom = random.choice(verify)

        generated = random.randint(1,99999999)



        total = f"{crandom}.{generated}.{vrandom}"
        print(f"[*] Generated Key: {total}")

        if total == "Carfulc.22222222.Token":
            print("WON")
            exit()











def mycnc():

    pc = os.getenv('COMPUTERNAME')
    print(f"Listening on port 4443...")
    print(""" 
    ********** Commands *************

    1. udpflood -- starts chrome
    2. tcp -- soon

    **********************************
    """)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 4443))

    server.listen(500)

    while True:
        client, addr = server.accept()
        print(client.recv(1024).decode())
        client.send("Server Connected.".encode())
        break

    while True:
        msg = input(f"{pc} : ")
        if msg == "EX":
            print("Quitting...")
            time.sleep(3)
            exit()
        os.system('cls')
        print("")
        print("")
        print("")
        client.send(f"{msg}".encode())
        print(client.recv(1024).decode())
        print("")
        print("")
        print("")













if __name__ == "__main__":
    print("""
    1. Check IP Alive     6. Encoder(Base64)
    2. Hostname to IP     7. Decoder(Base64)
    3. Proxy Generator    8. Random Timer
    4. HTML downloader    9. C2 Start
    5. Letter File Maker
    """)
    choice = int(input("Choice: "))
    if choice == 1:
        check()
    elif choice == 2:
        hostname()
    elif choice == 3:
        reqz()
    elif choice == 4:
        htmler()
    elif choice == 5:
        scraper()
    elif choice == 6:
        passbst()
    elif choice ==7:
        passdct()
    elif choice == 8:
        timr()
    elif choice == 9:
        mycnc()
    else:
        print("what?")