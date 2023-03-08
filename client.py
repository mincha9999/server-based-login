import socket
import time
import os

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 4444        # The port used by the server



def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def type_ani(text,speed):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(speed)

clear()
# Create a socket object
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    #connect to the server
    s.connect((HOST, PORT))


    # Get the username and password from the user
    username_send = input('Username: ')
    s.sendall(username_send.encode("utf-8"))
    password_send = input('Password: ')
    s.sendall(password_send.encode("utf-8"))

    print("trying to authenticate",end='')
    type_ani("...\n", speed=0.40)

    # Receive the response from the server
    response = s.recv(1024)
    # Print the response
    print(response.decode("utf-8"))
