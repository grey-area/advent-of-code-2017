from knot import knot_hash
import networkx as nx

key = 'ljoxqyyw'

graph = nx.Graph()
prev_row = None

for i in range(128):
    row_key = f'{key}-{i}'
    row_hex = knot_hash(row_key)
    row = f'{int(row_hex, 16):0128b}'
    for j in range(len(row)):
        if row[j] == '1':
            graph.add_edge((i, j), (i, j))
            if j > 0 and row[j - 1] == '1':
                graph.add_edge((i, j), (i, j - 1))
            if prev_row is not None and prev_row[j] == '1':
                graph.add_edge((i, j), (i - 1, j))
    prev_row = row

print(nx.number_connected_components(graph))
