from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer
from campo_minado_negocio import CampoMinado
from os.path import isfile
import json
import sys

OK = "200"
campo_minado = CampoMinado()

def criaJogo(linhas,colunas):
    campo_minado.criaJogo(linhas, colunas)
    return OK

def jogada(linha, coluna):
    campo_minado.jogada(linha, coluna)
    return OK

def qtdeJogadas():
    return campo_minado.qtdeJogadas()

def proseguir():
    return campo_minado.proximaJogada()

def mostraTabuleiro():
    return campo_minado.tabuleiro_show()

def server():
    serverRPC = SimpleJSONRPCServer(('localhost', 7002))
    serverRPC.register_function(criaJogo)
    serverRPC.register_function(jogada)
    serverRPC.register_function(proseguir)
    serverRPC.register_function(qtdeJogadas)
    serverRPC.register_function(mostraTabuleiro)
    print("Starting server")
    serverRPC.serve_forever()
