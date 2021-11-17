from collections import defaultdict

class Node:
  def __init__(self, value):
    self.adjacent = []
    self.value = value

def reverse_graph(graph):
  reversed = defaultdict(list)

  for _, node in graph.items():
    for adjacent in node.adjacent:
      reversed[adjacent.value].append(node.value)

  for k in graph:
    graph[k].adjacent = reversed[k]

  return graph

a = Node('a')
b = Node('b')
c = Node('c')

a.adjacent += [b, c]
b.adjacent += [c]

graph = {
    a.value: a,
    b.value: b,
    c.value: c,
}

for _, val in reverse_graph(graph).items():
  print(val.adjacent)