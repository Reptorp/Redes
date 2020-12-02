
"""
Created on Wed Dec  1 14:05:22 2020

@author: LUIS
"""

import heapq
import sys

class Graph:
    
    def __init__(self):
        self.vertices = {}
        
    def Agregar_vertice(self, nombre, linea):
        self.vertices[nombre] = linea
    
    def shortest_path(self, empezar, terminar):
        distancia = {} 
        antes = {}  
        nodos = [] 

        for vertex in self.vertices:
            if vertex == empezar: 
                distancia[vertex] = 0
                heapq.heappush(nodos, [0, vertex])
            else:
                distancia[vertex] = sys.maxsize
                heapq.heappush(nodos, [sys.maxsize, vertex])
            antes[vertex] = None
        
        while nodos:
            smallest = heapq.heappop(nodos)[1] 
            if smallest == terminar: 
                path = []
                while antes[smallest]: 
                    path.append(smallest)
                    smallest = antes[smallest]
                return path
            if distancia[smallest] == sys.maxsize:
                break
            
            for neighbor in self.vertices[smallest]:
                alt = distancia[smallest] + self.vertices[smallest][neighbor] 
                if alt < distancia[neighbor]: 
                    distancia[neighbor] = alt
                    antes[neighbor] = smallest
                    for n in nodos:
                        if n[1] == neighbor:
                            n[0] = alt
                            break
                    heapq.heapify(nodos)
        return distancia
        
    def __str__(self):
        return str(self.vertices)

if __name__ == '__main__':
    g = Graph()
    g.Agregar_vertice('A', {'B': 4, 'C': 5})
    g.Agregar_vertice('B', {'A': 4, 'F': 3})
    g.Agregar_vertice('C', {'A': 5, 'G': 6})  
    g.Agregar_vertice('F', {'B': 3, 'G': 9})
    g.Agregar_vertice('G', {'C': 6, 'F': 9})
    print(g.shortest_path('A', 'G'))