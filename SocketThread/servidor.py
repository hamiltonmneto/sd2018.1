import socket
from datetime import datetime
from ast import literal_eval
from campo_minado_negocio import CampoMinado
from consts_mensagem import QUANTIDADE_COLUNAS, QUANTIDADE_LINHAS, CODIGO_RESPOSTA, RESPOSTA_SUCESSO ,JOGADA_LINHA , CODIGO_COMANDO

ENCODE = "UTF-8"
MAX_BYTES = 65535
PORT = 5000
HOST = '127.0.0.1'
def servidor():
    orig = (HOST, PORT)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(orig)
    while True:
        data, address = sock.recvfrom(MAX_BYTES)
        mensagem = data.decode(ENCODE)
        contexto = literal_eval(mensagem)

        resposta = trataMensagem(contexto)
        data = resposta.encode(ENCODE)
        sock.sendto(data, address)

def trataMensagem(contexto):
    codigo = contexto["codigo_comando"]
    switch = {
       "1": novoJogo,
       "efetuar_jogada":jogada,
       "jogadas":quatidade,
       "tabuleiro":mostraTabuleiro
    }
    func = switch.get(str(codigo))
    return func(contexto)


def mostraTabuleiro(contexto):
    tabuleiro = jogo.MostrarTrabuleiro()
    return str(tabuleiro)

def quatidade(contexto):
    jogadas = jogo.qtdeJogadas()
    return str(jogadas)


def jogada(contexto):
    linha = int(contexto.get(JOGADA_LINHA))
    coluna = int(contexto.get(JOGADA_LINHA))
    jogo.jogada(linha,coluna)
    return str({CODIGO_RESPOSTA:RESPOSTA_SUCESSO})

def novoJogo(contexto):
    linha = int(contexto.get(QUANTIDADE_LINHAS))
    coluna = int(contexto.get(QUANTIDADE_COLUNAS))

    jogo.criaJogo(linha,coluna)
    tabu = jogo.MostrarTrabuleiro()
    return str(tabu)

if __name__ == "__main__":
    jogo = CampoMinado()
    servidor()
