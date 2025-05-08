import os
import requests
import asyncio
import threading
import socket
import time


url = "https://reqres.in/api/users?" #edit this url


def search(name):

    new_url = url + name

    print(f"Searching in {new_url}")
    response = requests.get(new_url)

    if response.status_code == 200:
        data = response.json()
        print(data)

    else:
        print(f"Data not found ({response.status_code})")


name = input("Enter what you want to search: ")
search(name)

















