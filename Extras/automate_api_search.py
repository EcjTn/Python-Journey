import requests

def search(name):

    print(f"Searching in {name}")
    response = requests.get(name)

    if response.status_code == 200:
        data = response.json()
        print(data)

    else:
        print(f"Data not found ({response.status_code})")


name = input("Enter what you want to search: ")
search(name)

















