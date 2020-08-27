from functools import reduce
from numpy import random

from br.cefet.NRainhas.IndividuoFactory import IndividuoFactory


class FGA:

    def rolota_viciada(self):
        pass

    def executar(nPop: int, nGeracoes: int, nElite: int, indFact: IndividuoFactory):
        popInicial = [indFact.get_individuo() for _ in range(nPop)]

        for g in range(1, nGeracoes + 1):
            filhos = []
            for i in range(0, len(popInicial), 2):
                filhos += popInicial[i].recombinar(popInicial[i + 1])

            mutantes = []
            for i in popInicial:
                mutantes.append(i.mutar())

            aux = popInicial + filhos + mutantes
            aux.sort(key=lambda x: x.get_avaliacao())

            newPop = []
            for i in range(nElite):
                if aux[i] not in newPop:
                    newPop.append(aux[i])

            # roleta viciada
            while len(newPop) < nPop:
                soma = reduce(lambda x, y: y + x, aux)
                roleta = random.random() * soma
                roletaParcial = 0
                j = 0
                while roletaParcial < roleta:
                    if aux[j].get_avaliacao() == 0:
                        roletaParcial += 0
                    else:
                        roletaParcial += 1. / aux[j].get_avaliacao()
                    j += 1

                if aux[j] not in newPop:
                    newPop.append(aux[j])

                aux.pop(j)

            popInicial = newPop
            print(f'Nº geração: {g}', end='. ')
            print(f'Melhor individuo: {popInicial[0]}')
