u"""Esse módulo possui a implementação de um servidor UDP."""
from socket import socket, AF_INET, SOCK_DGRAM

ENCODE = "UTF-8"
MAX_BYTES = 65535
PORT = 5000
HOST = ''

def server():
    u"""Essa função implementa um servidor que faz uso de um socket UDP"""

    orig = (HOST, PORT)
    sock = socket(AF_INET, SOCK_DGRAM)
    sock.bind(orig)

    while True:
        print("Ativando servidor ... ")
        data, address = sock.recvfrom(MAX_BYTES)
        text = data.decode(ENCODE)
        print("Recebemos a seguinte pergunta: " + text)

        text = "42"
        data = text.encode(ENCODE)
        sock.sendto(data, address)

if __name__ == "__main__":
    server()
            