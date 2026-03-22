import networkx as nx
import random
def weight_complete_graph(n):
    """
    Genera una gráfica completa con n vértices.
    Retorna un grafo NetworkX con pesos enteros aleatorios en las aristas.
    """
    G = nx.complete_graph(n)
    for u, v in G.edges():
        G[u][v]['weight'] = random.randint(10, 20)
    return G
def minimum_spanning_tree(G):
    """
    Calcula el árbol de expansión mínima de un grafo dado.
    Retorna un grafo NetworkX que representa el árbol de expansión mínima.
    Para esto se selecciona el peso mínimo de cada vértice 
    y se verifica que no forme ciclos.
    """

     
    