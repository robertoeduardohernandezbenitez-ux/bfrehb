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
    Verifica que el camino es conexo
    y se verifica que no forme ciclos y elimina los nodos ya explorados.
    """
    Gc = G.copy()
    T = nx.Graph() # Crear un nuevo grafo para el árbol de expansión mínima
    T.add_nodes_from(Gc.nodes())  # Agregar los mismos nodos al árbol de expansión mínima
    while len(T.edges())<len(Gc.nodes())-1: # Mientras el árbol de expansión mínima no tenga suficientes aristas   
        for u in Gc.nodes(): # Iterar sorbre cada nodo del grafo original
            min_weight = float('inf') # inicializar el peso minimo como infinito
            min_edge = None # inicializar la arista minima como None
            for v in Gc.neighbors(u): #iterar sobre los vecinos del nodo u
                weight = Gc[u][v]['weight'] # obtener el peso de la arista (u,v)
                if weight < min_weight: # si el peso es menor que el peso minimo actual
                    min_weight = weight # actualizar el peso minimo
                    min_edge = (u, v) # actualizar la arista minima
            if min_edge and not nx.has_path(T, min_edge[0], min_edge[1]): # si existe una arista minima y no forma un ciclo en el árbol de expansión mínima
                T.add_edge(min_edge[0], min_edge[1], weight=min_weight)  # agregar la arista minima al árbol de expansión mínima con su peso
                Gc.remove_edge(min_edge[0], min_edge[1]) # eliminar la arista de la grafica original para evitar seleccionarla nuevamente
    del Gc
    return T