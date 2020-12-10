from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import os
import sys


class Grafo(): 
  
    def __init__(self, vertices): 
        self.V = vertices 
        self.Grafo = [[0 for column in range(vertices)]  
                    for row in range(vertices)]
  

root = Tk()
root.title("Algoritmos Ambiciosos x Programação Dinâmica")


g = Grafo(9) 
g.Grafo = [[0, 4, 0, 0, 0, 0, 0, 8, 0], 
        [4, 0, 8, 0, 0, 0, 0, 11, 0], 
        [0, 8, 0, 7, 0, 4, 0, 0, 2], 
        [0, 0, 7, 0, 9, 14, 0, 0, 0], 
        [0, 0, 0, 9, 0, 10, 0, 0, 0], 
        [0, 0, 4, 14, 10, 0, 2, 0, 0], 
        [0, 0, 0, 0, 0, 2, 0, 1, 6], 
        [8, 11, 0, 0, 0, 0, 1, 0, 7], 
        [0, 0, 2, 0, 0, 0, 6, 7, 0] 
        ]; 


root.mainloop()
