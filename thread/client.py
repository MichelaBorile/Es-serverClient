import socket
import threading

def main():
    server_address = ("localhost", 6980)
    BUFFER_SIZE = 4092
    udp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_client_socket.bind(server_address)
    thread_invio = threading.Thread(target=invio, args=(udp_client_socket))
    thread_ricezione = threading.Thread(target=ricezione, args=(udp_client_socket))

    thread_invio.start()
    thread_ricezione.start()

def invio(udp_client_socket, server_addres):
    while(True):
        messaggio = input("")
        udp_client_socket.sendto(messaggio.encode(), server_addres)
def ricezione(udp_client_socket, BUFFER_SIZE):
    while(True):
        data, address = udp_client_socket.recvfrom(BUFFER_SIZE)
        print(f"risposta del server: {data.decode()} da {address}")
print(__name__)
if __name__ == "__main__":
    main()