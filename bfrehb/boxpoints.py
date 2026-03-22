import matplotlib.pyplot as plt
import networkx as nx
import random
from scipy.spatial.distance import euclidean

def unitary_box(n):
    "Crea una grafica de n puntos dentro de un cuadrado unitario y muestra su grafica"
    x=[ random.random() for i in range(n)]
    y=[ random.random() for i in range(n)]
    plt.plot(x,y,'ro')
    plt.axis([0,1,0,1])
    return plt.show()

def graph_in_box(n):
    """
    Crea una grafica completa de n puntos dentro del cuadrado unitario
    asigna sus pesos con la distancia euclidiana entre los puntos
    calcula su arbol generador de peso minimo
    muestra su grafica
    """
    x=[ random.random() for i in range(n)]
    y=[ random.random() for i in range(n)]
    points = list(zip(x, y))
    G = nx.complete_graph(n)
    for u, v in G.edges():
        G[u][v]['weight'] = euclidean(points[u], points[v])
    mtg = nx.minimum_spanning_tree(G)
    for u,v in mtg.edges():
        plt.plot( [points[u][0], points[v][0]], [points[u][1], points[v][1]], 'b-', linewidth=2)
    plt.plot(x,y,'ro')
    plt.axis([0,1,0,1])
    return plt.show()
