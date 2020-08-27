from br.cefet.NRainhas.NRainhasIndFactory import NRainhasIndFactory
from br.cefet.NRainhas.FGA import FGA


rainhas = 8
nPop = 10
nGeracoes = 1
nElite = 1
indFact = NRainhasIndFactory(rainhas)
FGA.executar(nPop, nGeracoes, nElite, indFact)
