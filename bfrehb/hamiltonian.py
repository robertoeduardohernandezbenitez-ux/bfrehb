import networkx as nx
from itertools import permutations

#This module provides functions to check for Hamiltonian cycles.
def is_hamiltonian_cycle(graph,cycle):
#Checks if the given cycle is a Hamiltonian cycle in the graph.
  n=len(set(cycle))
  if n != graph.order():
    return False
  for i in range(n-1):
    if not graph.has_edge(cycle[i],cycle[i+1]):
      return False
    if not graph.has_edge(cycle[n-1],cycle[0]):
      return False
  return True
#Checks if the graph has a Hamiltonian cycle by generating all permutations of vertices and checking each one.
def is_hamiltonian(graph):
  if not nx.is_connected(graph):
    return False
  vertices=list(graph.nodes())
  if len(vertices) <=2:
    return False
  perms= permutations(vertices)
  for perm in perms:
    if is_hamiltonian_cycle(graph,perm):
      return perm
  return False