import sys
from jsonrpclib import Server

GAME_OVER = "Game Over"

def menu():
    print("*****************************************")
    print("*              CAMPO MINADO             *")
    print("*****************************************")
    print("1 - INICIAR JOGO                         ")
    print("2 - SAIR                                 ")
    print("*****************************************\n")

def totalJogadas(proxy):
    qtd = proxy.qtdeJogadas()
    print(qtd)

def novoJogo(proxy):
    linha = int(input("Informe a quantidade de linhas: "))
    coluna =int(input("Informe a quantidade de colunas: "))
    proxy.criaJogo(linha, coluna)
    mostraTabuleiro(proxy.mostraTabuleiro())

def gameOver():
    print("*****************************************")
    print("*               GAME OVER               *")
    print("*****************************************")

def novaJogada(proxy):
    while proxy.continuar():
        qtd = proxy.qtdeJogadas()
        print("JOGADAS RESTESTANTES : ",qtd)
        linha = int(input("[Jogada]  Informe a  linha: "))
        coluna = int(input("[Jogada] Informe a coluna: "))
        if proxy.jogada(linha, coluna) == GAME_OVER:
            gameOver()
            return GAME_OVER
        mostraTabuleiro(proxy.mostraTabuleiro())
    return "Você Venceu!!!"

def sair(proxy):
    sys.exit()

def mostraTabuleiro(tabuleiro):
    for posicao in tabuleiro:
        print(str(posicao))

def client():
    proxy = Server('http://localhost:7002')
    switcher = {
        1: novoJogo,
        2: sair,
    }
    while True:
        menu()
        opcao = int(input("Opção escolhida: "))
        func = switcher.get(opcao)
        print(func(proxy))
