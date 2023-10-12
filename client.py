import socket
import time

#oprettter en socket til serveren
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8080))

#spørger brugeren om operation og tal1, tal2
operation = input("Vælg operation (Random/Add/Subtract): ")
num1 = input("Indtast tal1: ")
num2 = input("Indtast tal2: ")

#sender forespørgsel til serveren
request = f"{operation};{num1};{num2}"
client.send(request.encode())

#modtag og udskriv serverens svar
response = client.recv(1024).decode()
print(f"Serveren svarer: {response}")

#vent i nogle sekunder, så du har tid til at se svaret, før programmet lukker
time.sleep(3)

#luk klientforbindelsen
client.close()
