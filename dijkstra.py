# graph = {
#     'A': [('B', 1), ('C', 4)],
#     'B': [('A', 1), ('C', 2), ('D', 5)],
#     'C': [('A', 4), ('B', 2), ('D', 1)],
#     'D': [('B', 5), ('C', 1)]
# }

def dijkstra(graph, source, target):
  weights = {node: float('infinity') for node in graph}
  weights[source] = 0
  visited = set()
  predecessors = {node: None for node in graph}

  while len(visited) < len(graph):
    min_node = None
    min_weight = float('infinity')
    for node in graph:
      if node not in visited and weights[node] < min_weight:
        min_node = node
        min_weight = weights[node]

    if min_node is None:
      break

    visited.add(min_node)

    for neighbor, weight in graph[min_node]:
      total_weight = weights[min_node] + weight

      if total_weight < weights[neighbor]:
        weights[neighbor] = total_weight
        predecessors[neighbor] = min_node

  path = []
  current_node = target
  while current_node is not None:
    path.insert(0, current_node)
    current_node = predecessors[current_node]

  return {"minWeight": weights[target], "shortestPath": path}

