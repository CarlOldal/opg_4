import socket
import threading

#funktion til at behandle klientforbindelser
def handle_client(client_socket):
    request = client_socket.recv(1024).decode()
    response = process_request(request)
    client_socket.send(response.encode())
    client_socket.close()

#funktion til at behandle klientanmodninger
def process_request(request):
    parts = request.split(";")
    if len(parts) != 3:
        return "Invalid request format"

    operation, num1, num2 = parts[0], parts[1], parts[2]

    try:
        num1 = int(num1)
        num2 = int(num2)
    except ValueError:
        return "Invalid number format"

    if operation == "Random":
        import random
        result = random.randint(num1, num2)
    elif operation == "Add":
        result = num1 + num2
    elif operation == "Subtract":
        result = num1 - num2
    else:
        return "Invalid operation"

    return str(result)

#oprettter en socket til at lytte efter klientforbindelser
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 8080))
server.listen(5)

print("Serveren lytter på port 8080...")

#accepterer klientforbindelser og opretter tråd til hver klient
while True:
    client_sock, addr = server.accept()
    print(f"Accepteret forbindelse fra {addr[0]}:{addr[1]}")
    client_handler = threading.Thread(target=handle_client, args=(client_sock,))
    client_handler.start()
