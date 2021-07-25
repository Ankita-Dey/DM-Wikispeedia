import csv, os
import networkx as nx

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open("edges.csv", 'r') as f:
    edgelist = list(csv.reader(f))

G = nx.Graph()

G.add_edges_from(edgelist[1:])

cc = list(nx.connected_components(G))

output = []
components  = (G.subgraph(c).copy() for c in nx.connected_components(G))
for c in components:
    output.append([c.number_of_nodes(), c.number_of_edges(), nx.diameter(c)])

for _ in range(4604-G.number_of_nodes()):
    output.append([1, 0, 0])

output.sort()
output.insert(0, ['Nodes', 'Edges', 'Diameter'])
with open("graph-components.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(output)