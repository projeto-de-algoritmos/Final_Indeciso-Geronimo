from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import os
import sys


class Grafo(): 
  
    def __init__(self, vertices): 
        self.V = vertices 
        self.grafo = [[0 for column in range(vertices)]  
                    for row in range(vertices)]


    def printResultado(self, dist): 
        print("Vértice \tDistância até source")
        for node in range(self.V): 
            print("  ", node, "\t\t\t", dist[node]) 
  

    def minDistancia(self, dist, ArvMenorCaminho): 
  
        min = sys.maxsize 
  
        for v in range(self.V): 
            if dist[v] < min and ArvMenorCaminho[v] == False: 
                min = dist[v] 
                min_ind = v 
  
        return min_ind 
  

    def dijkstra(self, src): 
  
        dist = [sys.maxsize] * self.V 
        dist[src] = 0
        ArvMenorCaminho = [False] * self.V 
  
        for _ in range(self.V): 

            u = self.minDistancia(dist, ArvMenorCaminho) 
            ArvMenorCaminho[u] = True

            for v in range(self.V): 
                if self.grafo[u][v] > 0 and ArvMenorCaminho[v] == False and \
                dist[v] > dist[u] + self.grafo[u][v]: 
                    dist[v] = dist[u] + self.grafo[u][v] 
  
        self.printResultado(dist)  



if __name__ == '__main__':

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

    g.dijkstra(3)


    root.mainloop()
