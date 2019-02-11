from leitura import Leitura
import sys
import time
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

#encoding: utf-8


class Grafo():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def min_caminho(self, key, mstSet):  # caminho mínimo
        # print(key,mstSet)
        min = 1e99  # valor arbitrário

        for i in range(self.V):
            if key[i] < min and mstSet[i] == False:
                min = key[i]
                min_indice = i

        #print("INDICE:", min_indice)
        return min_indice

    def prim(self):  # matriz de adjacencia

        key = [1e99] * self.V
        parent = [None] * self.V
        key[0] = 0
        mst = [False] * self.V

        parent[0] = -1

        for i in range(self.V):
            u = self.min_caminho(key, mst)

            mst[u] = True

            for v in range(self.V):
                if self.graph[u][v] > 0 and mst[v] == False and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u
                    #print("chave: ",key[v],"\tparent", parent[v], "\n")

        self.imprimir(parent)

    def imprimir(self, parent):
        print("vertices \tPeso")
        soma = 0
        mintree = np.zeros([len(parent), 3], dtype=int)

        for i in range(len(parent)):
            mintree[i][0] = parent[i]
            mintree[i][1] = i
            mintree[i][2] = self.graph[i][parent[i]]
            soma += mintree[i][2]

        # for i in range(1, self.V):
        #    otimo += self.graph[i][parent[i]]
        #    print('{:5d}'.format(parent[i]), '{:5d}'.format(i), '\t', self.graph[i][parent[i]])
        print(mintree)
        print(soma)
        # print(otimo)


if __name__ == '__main__':
    param = sys.argv[1:]
    f = open(param[0], 'r')
    # inicio=time.time()
    g = Leitura()
    g.procura(f)
    vertice = g.vertice[0]
    ver = Grafo(vertice)
    ver.graph = g.adj
    ver.prim()

    #fim = time.time()
    #print(fim-inicio, 'ms')
