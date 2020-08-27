from br.cefet.NRainhas.Individuo import Individuo
from numpy.random import permutation
from numpy import ndarray
from numpy import zeros
from numpy import random
from numpy import where


class NRainhasInd(Individuo):

    def __init__(self, nRainhas, rand=True):
        super().__init__(-1)
        self.__nRainhas = nRainhas
        self.__genes = ndarray([])

        if rand:
            self.__genes = permutation(range(1, self.__nRainhas + 1))
        else:
            self.__genes = zeros(nRainhas, dtype=int)

    def recombinar(self, ind):
        corte: int = random.randint(1, self.__nRainhas)
        F1 = NRainhasInd(self.__nRainhas, False)
        F2 = NRainhasInd(self.__nRainhas, False)

        genes = zeros(self.__nRainhas, dtype=int)
        for i in range(0, corte):
            genes[i] = self.__genes[i]

        for i in range(corte, self.__nRainhas):
            if ind.get_genes()[i] not in genes:
                genes[i] = ind.get_genes()[i]

        for i in range(self.__nRainhas):
            if i + 1 not in genes:
                index = where(genes == 0)
                genes[index[0][0]] = i + 1
        F1.__genes = genes

        genes = zeros(self.__nRainhas, dtype=int)
        for i in range(0, corte):
            genes[i] = ind.get_genes()[i]

        for i in range(corte, self.__nRainhas):
            if self.get_genes()[i] not in genes:
                genes[i] = self.get_genes()[i]

        for i in range(self.__nRainhas):
            if i + 1 not in genes:
                index = where(genes == 0)
                genes[index[0][0]] = i + 1
        F2.__genes = genes
        ret = [F1, F2]
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

    def get_avaliacao(self) -> int:
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

    def get_genes(self):
        return self.__genes

    def __add__(self, other) -> float:
        if not isinstance(other, float):
            other = float(other.get_avaliacao())

        if self.get_avaliacao() != 0 and other != 0:
            return 1./self._avaliacao + 1./other
        elif self.get_avaliacao() != 0 and other == 0:
            return 1./self._avaliacao
        elif self.get_avaliacao() == 0 and other != 0:
            return 1./other
        else:
            return 0.0

    def __str__(self):
        return f'avaliacao: {self._avaliacao}, ' \
               f'genes: {self.__genes}'
