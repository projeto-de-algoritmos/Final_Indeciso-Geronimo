from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import os
import sys


class Grafo(): 
  
    def __init__(self, vertices): 
        self.V = vertices 
        self.grafo = [[0 for coluna in range(vertices)]  
                    for linha in range(vertices)]


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
            print("\n%d --> %d \t\t  %d \t\t " % (src, i, dist[i]), end='') 
            self.printCaminho(parent,i)
            print("")
  

    def dijkstra(self, grafo, src): 
  
        linha  = len(grafo) 
        coluna = len(grafo) 
   
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
                if grafo[u][i] and i in fila: 
                    if dist[u] + grafo[u][i] < dist[i]: 
                        dist[i] = dist[u] + grafo[u][i] 
                        parent[i] = u 
  
  
        # print the constructed distance array 
        self.printResultado(dist,parent,src)  


root = Tk()
root.title("Algoritmos Ambiciosos x Programação Dinâmica")

g = Grafo(9) 
g.grafo = [[0, 4, 0, 0, 0, 0, 0, 8, 0], 
               [4, 0, 8, 0, 0, 0, 0, 11, 0], 
               [0, 8, 0, 7, 0, 4, 0, 0, 2], 
               [0, 0, 7, 0, 9, 14, 0, 0, 0], 
               [0, 0, 0, 9, 0, 10, 0, 0, 0], 
               [0, 0, 4, 14, 10, 0, 2, 0, 0], 
               [0, 0, 0, 0, 0, 2, 0, 1, 6], 
               [8, 11, 0, 0, 0, 0, 1, 0, 7], 
               [0, 0, 2, 0, 0, 0, 6, 7, 0] 
              ];

g.dijkstra(g.grafo,0)

exit()


root.mainloop()
