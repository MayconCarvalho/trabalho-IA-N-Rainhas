from br.cefet.NRainhas.NRainhasIndFactory import NRainhasIndFactory
from br.cefet.NRainhas.FGA import FGA


if __name__ == '__main__':
    rainhas = 9
    nPop = 40
    nGeracoes = 10
    nElite = 6
    indFact = NRainhasIndFactory(rainhas)
    FGA.executar(nPop, nGeracoes, nElite, indFact)
