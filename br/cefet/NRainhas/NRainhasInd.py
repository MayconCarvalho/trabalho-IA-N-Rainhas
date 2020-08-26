from br.cefet.NRainhas.Individuo import Individuo
from numpy.random import permutation
from numpy import ndarray
from numpy import zeros
from numpy import random


class NRainhasInd(Individuo):

    def __init__(self, nRainhas, rand=True):
        super().__init__(-1)
        self.__nRainhas = nRainhas
        self.__genes = ndarray([])

        if rand:
            self.__genes = permutation(range(1, self.__nRainhas + 1))
        else:
            self.__genes = zeros(nRainhas)

    def recombinar(self, ind):
        ret = []
        return ret

    def mutar(self):
        mut = NRainhasInd(self.__nRainhas, False)
        ind1 = random.randint(self.__nRainhas)
        ind2 = random.randint(self.__nRainhas)

        while ind2 == ind1:
            ind2 = random.randint(self.__nRainhas)

        genesAux = self.__genes
        aux = genesAux[ind1]
        genesAux[ind1] = genesAux[ind2]
        genesAux[ind2] = aux
        mut.__genes = genesAux

        return mut

    def get_avaliacao(self):
        if self._avaliacao == -1:
            self._avaliacao = 0
            for i in range(self.__nRainhas):
                for j in range(i + 1, self.__nRainhas):
                    if self.__genes[i] == self.__genes[j]:
                        self._avaliacao += 1
                    if self.__genes[i] == (self.__genes[j] - abs(j - i)):
                        self._avaliacao += 1
                    if self.__genes[i] == (self.__genes[j] + abs(j - i)):
                        self._avaliacao += 1

        return self._avaliacao

    def __str__(self):
        return f'avaliacao: {self._avaliacao}, ' \
               f'genes: {self.__genes}, ' \
               f'NRainhas: {self.__nRainhas}'
