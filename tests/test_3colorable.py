from bfrehb import is_3_colorable
import networkx as nx

def test_3_colorable():
    G=nx.Graph()
    G.add_edges_from([(0,1),(1,2),(2,0)])
    assert is_3_colorable(G)==(0, 1, 2)
    
    G=nx.Graph()
    G.add_edges_from([(0,1),(1,2),(2,3),(3,0),(0,2),(1,3)])
    assert is_3_colorable(G)==False