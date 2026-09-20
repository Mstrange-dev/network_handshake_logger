import socket

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
print(f'Hostname: {hostname}')
print(f'IP: {ip}')


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("", 9999))
server_socket.listen()

print(f"Server is up and listening on {ip}:9999...")

try:
    while True:

        client_socket, client_address = server_socket.accept()
        print(f"[+] TCP Handshake successful! Connection received from: {client_address}")
        
      
        client_socket.close()

except KeyboardInterrupt:
    print("\n[!] Shutting down server...")
    server_socket.close()
    print("[*] Server socket closed safely.")