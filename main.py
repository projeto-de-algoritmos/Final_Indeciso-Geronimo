from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import os
import sys
from timeit import default_timer as timer
import matplotlib.pyplot as plt 

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
  

    def dijkstra(self, src, destination): 
  
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
  
  
        #self.printResultado(dist,parent,src)
        return str(dist[destination]), parent


    def printArr(self, dist, destination):

        print("Vértice \tDistância até Source")  
        for i in range(1, self.V):  
            print("{0} \t\t\t  {1}".format(i, dist[destination]))


    def BellmanFord(self, src, destination):  
   
        dist = [float("Inf")] * self.V  
        dist[src] = 0
  
        for _ in range(self.V - 1):  

            for u, v, w in self.grafoDP:  
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:  
                    dist[v] = dist[u] + w  

        return str(dist[destination])

    

g = Grafo(9)
g.addEdge(0, 1, 4)
g.addEdge(0, 7, 8)

g.addEdge(1, 0, 4)
g.addEdge(1, 2, 8)
g.addEdge(1, 7, 11)

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

           # 0  1  2  3  4  5  6  7  8
g.grafo = [ [0, 4, 0, 0, 0, 0, 0, 8, 0],   # 0
            [4, 0, 8, 0, 0, 0, 0, 11, 0],  # 1
            [0, 8, 0, 7, 0, 4, 0, 0, 2],   # 2
            [0, 0, 7, 0, 9, 14, 0, 0, 0],  # 3
            [0, 0, 0, 9, 0, 10, 0, 0, 0],  # 4
            [0, 0, 4, 14, 10, 0, 2, 0, 0], # 5
            [0, 0, 0, 0, 0, 2, 0, 1, 6],   # 6
            [8, 11, 0, 0, 0, 0, 1, 0, 7],  # 7
            [0, 0, 2, 0, 0, 0, 6, 7, 0]    # 8
          ]


root = Tk()
root.geometry("600x860")
root.title("Algoritmos Ambiciosos x Programação Dinâmica")

subtitulo = Label(root, text="\nBairo São Bernardo\n")
subtitulo.pack()

imagem = Image.open("image.png").resize((530, 300), Image.ANTIALIAS)
imagem = ImageTk.PhotoImage(imagem)
imgLabel = Label(image=imagem)
imgLabel.pack(padx=35)


def buscar():
    origem = int(opc_origem.get())
    destino = int(opc_destino.get())
    
    dijkstra, parent = g.dijkstra(origem, destino)
    bellmanford = g.BellmanFord(origem, destino)

    resultDijkstra.config(text=dijkstra)
    resultBellmanFord.config(text=bellmanford)


label = Label(text="\n\nEscolha o ponto de início:\n")
label.pack()
options = range(0,9)
opc_origem = StringVar()
opc_origem.set(options[0])

possiveis_nos = OptionMenu(root, opc_origem, *options)
possiveis_nos.pack(padx=100)

label = Label(text="Escolha o ponto de destino:\n")
label.pack()
options = range(0,9)
opc_destino = StringVar()
opc_destino.set(options[0])

possiveis_nos = OptionMenu(root, opc_destino, *options)
possiveis_nos.pack(padx=100)

fazerBuscas = Button(root, text="Gerar caminho mais curto", command=buscar)
fazerBuscas.pack(pady=20)

label = Label(
    text="_________________________________________________________________")
label.pack()

label = Label(
    text="\nRESULTADOS")
label.pack()

DijkstraLabel = Label(root, text="\nDijkstra:", pady=5)
DijkstraLabel.pack()
global resultDijkstra
resultDijkstra = Label(root, text="", wraplength=600, pady=5, padx=20)
resultDijkstra.pack()

BellmanFordLabel = Label(root, text="BellmanFord:", pady=5)
BellmanFordLabel.pack()
global resultBellmanFord
resultBellmanFord = Label(root, text="", wraplength=600, pady=5, padx=20)
resultBellmanFord.pack()

CaminhoLabel = Label(root, text="Caminho percorrido:", pady=5)
CaminhoLabel.pack()
global Caminho
Caminho = Label(root, text="", wraplength=600, pady=5, padx=20)
Caminho.pack()

root.mainloop()