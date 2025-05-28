import sys
import os
import socket

######### simple project scanner test with range input -- ecjt ##############

target = input("Enter IP: ")
start_port = int(input("Enter Start port RANGE (ex. 1): "))
end_port = int(input("Enter End port (ex. 65535): "))

print("_" * 50)
print("")
print(f"Scanning: {target} : {start_port}-{end_port}")
print("_" * 50)
print("")


for port in range(start_port, end_port):
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(0.5)
        client.connect((target, port))
        client.close()
        collected = f"[*] {target}:{port} Open"
        print(f"[*] {target}:{port} Open")
        with open("OpenPorts.txt", "a") as f:
            f.write(f"{collected} \n")


    except Exception as e:
        print(f"Error: {e}")
