import networkx as nx

with open('input') as f:
    data = f.read().splitlines()

graph = nx.Graph()

for line in data:
    x, ys = line.split(' <-> ')
    y_list = ys.split(', ')
    for y in y_list:
        graph.add_edge(int(x), int(y))

print(len(nx.node_connected_component(graph, 0)))
