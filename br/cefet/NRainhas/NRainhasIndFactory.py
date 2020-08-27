from br.cefet.NRainhas.IndividuoFactory import IndividuoFactory
from br.cefet.NRainhas.NRainhasInd import NRainhasInd


class NRainhasIndFactory(IndividuoFactory):

    def __init__(self, nRainhas: int):
        self.__nRainhas = nRainhas

    def get_individuo(self) -> NRainhasInd:
        return NRainhasInd(self.__nRainhas)
