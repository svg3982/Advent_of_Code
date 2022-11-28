import networkx as nx
import matplotlib.pyplot as plt
from re import match

G = nx.Graph()
paths = []

with open('dec12_test_input.txt') as ip:
    for line in ip:
        line = line.replace("\n", "")
        line = line.split("-")
        pos = list(map(str, line))
        paths.append(pos)
ip.close()
print(paths)

caves = set([item for sublist in paths for item in sublist])
big_caves = list(filter(lambda v: match('[A-Z]+', v), caves))
small_caves = list(filter(lambda v: match('[a-z]+', v), caves))
print(big_caves, small_caves)

for i in caves:
    check_size = "big" if i in big_caves else "small"
    G.add_node(i,size=check_size)
#fill graph

G.add_edges_from(paths)

#testing
print(G.nodes(data=True))
print("nodes",G.nodes,"edges", G.edges, "size",list(nx.get_node_attributes(G,"size"))[0])
print("breadth first:", list(nx.bfs_edges(G,'start')))
for path in nx.all_simple_paths(G, source='start', target='end'): print(path)
print("dijkstra:", list(nx.bidirectional_shortest_path(G,'start','end')))

