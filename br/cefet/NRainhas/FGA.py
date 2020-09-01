from functools import reduce
from numpy import random

from br.cefet.NRainhas.IndividuoFactory import IndividuoFactory


class FGA:

    def executar(nPop: int, nGeracoes: int, nElite: int, indFact: IndividuoFactory):
        # criando a população inicial com genes aleatorios
        popInicial = [indFact.get_individuo() for _ in range(nPop)]

        for g in range(1, nGeracoes + 1):
            # tamanho da lista de individuos recombinados e mutantes
            tam = nPop if nPop % 2 == 0 else nPop - 1

            # criando a lista filhos por recombinação e adicionando na lista
            filhos = []
            for i in range(0, tam, 2):
                filhos += popInicial[i].recombinar(popInicial[i + 1])

            # criado a lista de mutantes e adicionado na lista
            mutantes = []
            for i in range(tam):
                mutantes.append(popInicial[i].mutar())

            # contanenando todas as listas de individuos
            aux = popInicial + filhos + mutantes

            # calculando a avaliacao de cada individuo e ordenando a lista
            aux.sort(key=lambda x: x.get_avaliacao())

            # criado lista de nova populacao (newPop)
            newPop = []

            # adicionando os individuos de elite na lista newPop
            j = 0
            while len(newPop) < nElite:
                if aux[j] not in newPop:
                    newPop.append(aux[j])
                    aux.pop(j)
                j += 1

            # roleta viciada adicionado os outros individuos na lista
            while len(newPop) < nPop:
                # soma das avaliacoes de todos os individuos
                soma = reduce(lambda x, y: y + x, aux)
                # valor aleatorio gerado pela roleta
                roleta = random.random() * soma
                roletaParcial = 0
                j = 0
                while roletaParcial < roleta:
                    if aux[j].get_avaliacao() != 0:
                        roletaParcial += 1. / aux[j].get_avaliacao()
                    j += 1

                if aux[j] not in newPop:
                    newPop.append(aux[j])

                aux.pop(j)

            popInicial = newPop
            print(f'Nº geração: {g}', end='. ')
            print(f'Melhor individuo: {popInicial[0]}')
