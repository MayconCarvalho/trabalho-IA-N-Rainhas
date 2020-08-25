from br.cefet.NRainhas.Individuo import Individuo


class NRainhasInd(Individuo):

    def __init__(self, nRainhas, rand=True):
        super().__init__(-1)
        self.__nRainhas = nRainhas
        self.__genes = []

        if rand:
            pass

    def recombinar(self, ind):
        ret = []
        return ret

    def mutar(self):
        mut = NRainhasInd(self.__nRainhas)
        return mut

    def get_avaliacao(self):
        if self._avaliacao == -1:
            return self._avaliacao
