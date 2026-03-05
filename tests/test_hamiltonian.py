from bfrehb import is_hamiltonian
import networkx as nx

def test_hamiltonian():
    G=nx.Graph()
    G.add_edges_from([(0,1),(1,2),(2,3),(3,0),(0,2)])
    assert is_hamiltonian(G)==(0, 1, 2, 3)

    G=nx.Graph()
    G.add_edges_from([(0,1),(1,2),(2,3)])
    assert is_hamiltonian(G)==False