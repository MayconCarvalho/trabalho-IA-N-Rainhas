from br.cefet.NRainhas.NRainhasIndFactory import NRainhasIndFactory
from br.cefet.NRainhas.FGA import FGA


rainhas = 8
nPop = 40
nGeracoes = 10
nElite = 3
indFact = NRainhasIndFactory(rainhas)
FGA.executar(nPop, nGeracoes, nElite, indFact)
