from random import randint
from os.path import isfile
from os import remove
import json

class CampoMinado:

    def criaJogo(self, linha, coluna):
        self.__linha = linha
        self.__coluna = coluna
        self.__total_jogadas = (linha * coluna) - self.__totalBombas(linha, coluna)
        self.__tabuleiro = self.__iniciaTabuleiro(linha, coluna)
        self.__coordenadas_bombas = self.__distribuiBombas(linha,coluna)

    def __totalBombas(self, linha, coluna):
        return int((linha*coluna)/3)        

    def __iniciaTabuleiro(self, linha, coluna):
        return [['*' for x in range(coluna)] for j in range(linha)]

    def __distribuiBombas(self, linha, coluna):
        quantidade_bombas = self.__totalBombas(linha, coluna)
        coordenadas_bombas = []
        while quantidade_bombas > 0:
            coordenada = (randint(0, linha - 1), randint(0, coluna - 1))
            if coordenada not in coordenadas_bombas:
                coordenadas_bombas.append(coordenada)
                quantidade_bombas-=1
        return coordenadas_bombas


    def imprimirTabuleiro(self):
        for posicao in self.__tabuleiro:
            return (str(posicao))

    def MostrarTrabuleiro(self):
        return str(self.__tabuleiro)

    def _validaCordenadas(self, linha, coluna):
        if linha not in range(0, self.__linha):
            print("linha invalida")
            return False
        elif coluna not in range(0, self.__coluna):
            print("coluna invalida")
            return False
        return True

    def _contaBombasVizinho(self, linha, coluna):
        bombas = 0
        for line in range(linha-1, linha+1):
            for col in range(coluna-1, coluna+1):
                posicao = (line, col)
                if posicao in self.__coordenadas_bombas:
                    bombas += 1
        return str(bombas)

    def _marcaJogada(self, linha, coluna):
        marcador = self._contaBombasVizinho(linha, coluna)
        self.__tabuleiro[linha][coluna] = marcador
        #self.imprimirTabuleiro()

    def proximaJogada(self):
        return self.__total_jogadas > 0

    def gameOver(self):
         print("-----------------VOCÊ ACERTOU UMA MINA---------------")
         print("------------------------GAME OVER--------------------")
         print("-------------------------------------------------\n\n")

    def qtdeJogadas(self):
        return self.__total_jogadas

    def jogada(self, linha, coluna):
        if self._validaCordenadas(linha, coluna):
            posicao = (linha, coluna)
            if posicao in self.__coordenadas_bombas:
                self.__total_jogadas = 0
            else:
                self._marcaJogada(linha, coluna)
                self.__total_jogadas -= 1
