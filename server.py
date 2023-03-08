import socket
import os

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 4444       # The port used by the server





# Create a socket object
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    print('Server Started on', HOST, ":", PORT)

    # Listen for incoming connections
    s.listen()
    print("listening for connections...")
    


    while True:
        # Accept a connection and create a new socket object to handle it
        conn, addr = s.accept()
        with conn:
            print('Someone Connected by', addr)

            # Receive the username from the client
            username_recived = conn.recv(1024).decode()
            print(f"recived <Username> from {addr}")

            # Receive the password from the client
            password_recived = conn.recv(1024).decode()
            print(f"recived <password> from {addr}")


            print("varifying authentication...")

            #open password file
            with open('password.krypted', 'r') as file:
                line_number_password = 2
                for i in range(line_number_password):
                    password = file.readline().strip()

            with open('password.krypted', 'r') as file:
                line_number_username = 4
                for i in range(line_number_username):
                    userename = file.readline().strip()
            
            

            # Check if the username and password are valid
            if username_recived == userename and password_recived == password:
                # Send a success message to the client
                conn.sendall("Access Granted!".encode("utf-8"))
                print(f"{addr} succesfully logged in!")
                
            else:
                # Send a failure message to the client
                conn.sendall("Access Denied!".encode("utf-8"))

                print(f"{addr} failed to log in!")
                print("reason:")
                if username_recived == userename:
                    print(">    <username> mached! ")
                else:
                    print(">    <username> did not match! ")
                if password_recived == password:
                    print(">    <password> mached! ")
                else:
                    print(">    <password> did not match!")

                print()
