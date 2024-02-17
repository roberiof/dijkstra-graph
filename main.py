import networkx as nx
import random
from dijkstra import *


# Read GML file
graphGML = nx.read_gml("data/polblogs.gml")

# Get all nodes
nodes = []
for node_id, attributes in graphGML.nodes(data=True):
    nodes.append(node_id)

# Build Graph
graph = {node: [] for node in nodes}
for edge in graphGML.edges(data=True):
    source = edge[0]
    target = edge[1]
    weight = random.uniform(0,10)
    if source not in graph:
      graph[source] = []

    graph[source].append((target, weight))

sourceBlog = input("Escolha o blog de início: ").strip()
targetBlog = input("Escolha o blog final: ").strip()

if (sourceBlog != targetBlog and sourceBlog in graph and targetBlog in graph):
  shortest_distances = dijkstra(graph, sourceBlog)
  print(f"O menor caminho entre os blogs {sourceBlog} e {targetBlog} é: {shortest_distances[targetBlog]}")

