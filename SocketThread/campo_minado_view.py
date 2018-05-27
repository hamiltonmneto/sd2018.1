from campo_minado_negocio import CampoMinado
from os.path import isfile
from os import remove
import json
import sys
from consts_mensagem import QUANTIDADE_COLUNAS, QUANTIDADE_LINHAS

def menuInicial():
    print("*****************************************")
    print("*              CAMPO MINADO             *")
    print("*****************************************")
    print("1 - INICIAR JOGO                         ")
    print("2 - SAIR                                 ")
    print("*****************************************\n")

def novoJogo(contexto):
    contexto[QUANTIDADE_LINHAS] = input("Informe a quantidade de linhas: ")
    contexto[QUANTIDADE_COLUNAS] = input("Informe a quantidade de colunas: ")
    return str(contexto)

def sair(contexto):
    sys.exit(0)

def mostraQuantidadeJogadas(valor):
    if valor == '0':
        print('Game Over')
    else:
        print('Quantidade de Jogadas: ', valor)
