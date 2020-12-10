from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import os
import sys
from timeit import default_timer as timer


class Grafo(): 
  
    def __init__(self, vertices): 
        self.V = vertices 
        self.grafo = [[0 for coluna in range(vertices)]  
                    for linha in range(vertices)]
        self.grafoDP = []


    def addEdge(self, u, v, w):  
        self.grafoDP.append([u, v, w])


    def minDistancia(self,dist,fila): 

        min = float("Inf") 
        min_ind = -1
         
        for i in range(len(dist)): 
            if dist[i] < min and i in fila: 
                min = dist[i] 
                min_ind = i 
        return min_ind
  

    def printCaminho(self, parent, j): 

        if parent[j] == -1:
            print(j, ", ", end='')
            return
        self.printCaminho(parent , parent[j]) 
        print(j, ", ", end='') 
          
 
    def printResultado(self, dist, parent, src):

        print("Vértice \tDistância até Source\tCaminho") 
        for i in range(1, len(dist)): 
            print("%d --> %d \t\t  %d \t\t " % (src, i, dist[i]), end='') 
            self.printCaminho(parent,i)
            print("")
  

    def dijkstra(self, src): 
  
        linha  = len(self.grafo) 
        coluna = len(self.grafo) 
   
        dist = [float("Inf")] * linha 
        parent = [-1] * linha 
        dist[src] = 0
      
        fila = [] 
        for i in range(linha): 
            fila.append(i) 
 
        while fila: 
  
            u = self.minDistancia(dist,fila)       
            fila.remove(u) 

            for i in range(coluna):
                if self.grafo[u][i] and i in fila: 
                    if dist[u] + self.grafo[u][i] < dist[i]: 
                        dist[i] = dist[u] + self.grafo[u][i] 
                        parent[i] = u 
  
  
        # print the constructed distance array 
        self.printResultado(dist,parent,src)


    def printArr(self, dist):

        print("Vértice \tDistância até Source")  
        for i in range(1, self.V):  
            print("{0} \t\t\t  {1}".format(i, dist[i]))


    def BellmanFord(self, src):  
   
        dist = [float("Inf")] * self.V  
        dist[src] = 0
  
        for _ in range(self.V - 1):  

            for u, v, w in self.grafoDP:  
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:  
                    dist[v] = dist[u] + w  
   
        self.printArr(dist) 


if __name__ == '__main__':
    

    g = Grafo(9)
    g.addEdge(0, 1, 4)
    g.addEdge(0, 7, 8)

    g.addEdge(1, 0, 4)
    g.addEdge(1, 2, 8)
    g.addEdge(1, 1, 11)

    g.addEdge(2, 1, 8)
    g.addEdge(2, 3, 7)
    g.addEdge(2, 5, 4)
    g.addEdge(2, 8, 2)

    g.addEdge(3, 2, 7)
    g.addEdge(3, 4, 9)
    g.addEdge(3, 5, 14)

    g.addEdge(4, 3, 9)
    g.addEdge(4, 5, 10)

    g.addEdge(5, 2, 4)
    g.addEdge(5, 3, 14)
    g.addEdge(5, 4, 10)
    g.addEdge(5, 6, 2)

    g.addEdge(6, 5, 2)
    g.addEdge(6, 7, 1)
    g.addEdge(6, 8, 6)

    g.addEdge(7, 0, 8)
    g.addEdge(7, 1, 11)
    g.addEdge(7, 6, 1)
    g.addEdge(7, 8, 7)

    g.addEdge(8, 2, 2)
    g.addEdge(8, 6, 6)
    g.addEdge(8, 7, 7)


    g.grafo = [ [0, 4, 0, 0, 0, 0, 0, 8, 0], 
                [4, 0, 8, 0, 0, 0, 0, 11, 0], 
                [0, 8, 0, 7, 0, 4, 0, 0, 2], 
                [0, 0, 7, 0, 9, 14, 0, 0, 0],
                [0, 0, 0, 9, 0, 10, 0, 0, 0],
                [0, 0, 4, 14, 10, 0, 2, 0, 0],
                [0, 0, 0, 0, 0, 2, 0, 1, 6],
                [8, 11, 0, 0, 0, 0, 1, 0, 7],
                [0, 0, 2, 0, 0, 0, 6, 7, 0] 
              ]


    start = timer()
    g.dijkstra(0)
    end = timer()
    time_dijkstra = end - start
    print("Dijkstra = %.7f" % time_dijkstra, " seg")

    start = timer()
    g.BellmanFord(0)
    end = timer()
    time_bellmanford = end - start
    print("BellmanFord = %.7f" % time_bellmanford, " seg")

    time_diff = abs(time_dijkstra - time_bellmanford)

    if(time_dijkstra < time_bellmanford):
        print("BellmanFord foi melhor por %.7f" % time_diff, " seg")
    else:
        print("Dijkstra foi melhor por %.7f" % time_diff, " seg")

    exit()

    root.mainloop()
