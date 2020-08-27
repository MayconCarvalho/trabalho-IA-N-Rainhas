from br.cefet.NRainhas.IndividuoFactory import IndividuoFactory


class FGA:

    def relota_viciada(self):
        pass

    def executar(nPop: int, nGeracoes: int, nElite: int, indFact: IndividuoFactory):
        popInicial = [indFact.get_individuo() for _ in range(nPop)]

        for g in range(nGeracoes):
            filhos = []
            for i in range(0, len(popInicial), 2):
                filhos += popInicial[i].recombinar(popInicial[i + 1])

            mutantes = []
            for i in popInicial:
                mutantes.append(i.mutar())

            aux = popInicial + filhos + mutantes
            aux.sort(key=lambda x: x.get_avaliacao())
            print('listao')
            [print(i) for i in aux]

            newPpo = []
            for i in range(nElite):
                if aux[i] not in newPpo:
                    newPpo.append(aux[i])

