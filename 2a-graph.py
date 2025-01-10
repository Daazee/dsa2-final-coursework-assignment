import networkx as nx
import matplotlib.pyplot as mp

G = nx.Graph()

nodes = ["A", "B", "C", "D", "E", "F", "G", "Z"]
G.add_nodes_from(nodes)
G.add_edge("A", "B", weight=1)
G.add_edge("A", "C", weight=5)
G.add_edge("A", "G", weight=10)
G.add_edge("B", "D", weight=3)
G.add_edge("C", "D", weight=8)
G.add_edge("C", "E", weight=6)
G.add_edge("C", "Z", weight=9)
G.add_edge("D", "F", weight=1)
G.add_edge("E", "G", weight=3)
G.add_edge("E", "Z", weight=1)
G.add_edge("F", "Z", weight=6)

pos = nx.spring_layout(G, seed=7)  # positions for all nodes - seed for reproducibility

# draw nodes
nx.draw_networkx_nodes(G, pos, node_size=700)

# draw edges
nx.draw_networkx_edges(G, pos, width=2, style="solid")

# draw node labels
nx.draw_networkx_labels(G, pos, font_size=14)

# draw edge weight labels
edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels)

#Remove the rectangular box housing the graph
mp.axis("off")

mp.show()