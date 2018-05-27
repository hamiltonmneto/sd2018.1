u"""Esse módulo possui a implementação de um cliente UDP. """
from socket import socket, AF_INET, SOCK_DGRAM

ENCODE = "UTF-8"
MAX_BYTES = 65535
PORT = 5000
HOST = '127.0.0.1'
def client():
    u"""Procedimento responsável por enviar dados para o servidor e receber alguma resposta por conta disso."""

    text = "Qual o sentido da vida ?"
    data = text.encode(ENCODE)

    sock = socket(AF_INET, SOCK_DGRAM)
    dest = (HOST, PORT)
    sock.sendto(data, dest)
    print("Mensagem enviada, esperando resposta")

    data, address = sock.recvfrom(MAX_BYTES)
    text = data.decode(ENCODE)
    print("A resposta foi: " + text)
    sock.close() #Fechando Socket

if __name__ == "__main__":
    client()



