import networkx as nx
import matplotlib.pyplot as mp

#check if the supplied graph has a cycle.
def isCycle(graph):
    try:
        nx.find_cycle(graph)
        return True
    except:
        return False

original_graph = nx.Graph()

original_graph_nodes = ["A", "B", "C", "D", "E", "F", "G", "Z"]
original_graph.add_nodes_from(original_graph_nodes)
original_graph.add_edge("A", "B", weight=1)
original_graph.add_edge("A", "C", weight=5)
original_graph.add_edge("A", "G", weight=10)
original_graph.add_edge("B", "D", weight=3)
original_graph.add_edge("C", "D", weight=8)
original_graph.add_edge("C", "E", weight=6)
original_graph.add_edge("C", "Z", weight=9)
original_graph.add_edge("D", "F", weight=1)
original_graph.add_edge("E", "G", weight=3)
original_graph.add_edge("E", "Z", weight=1)
original_graph.add_edge("F", "Z", weight=6)

#using Kruskal algorithm
sorted_edges=sorted(original_graph.edges(data=True), key=lambda edge: edge[2].get('weight', 1))
original_graph_edges_length = len(original_graph.edges())

MST = nx.Graph()
mstValue = 0
for i in range(0,original_graph_edges_length):
   number_of_edges = len(MST.edges)
   if(number_of_edges == len(original_graph_nodes)-1): #check if the number of MST edges is less than k-1 as defined in our MST class
      break
   
   node_detail_with_weight = sorted_edges[i] #get the current nodes, edges and their weifgh
   fromNode = node_detail_with_weight[0] #node 1
   toNode =node_detail_with_weight[1] #node 2
   edgeWeight = node_detail_with_weight[2]["weight"] #edge weight
   
   mstValue = mstValue + edgeWeight #add the edge weight to determine the MST value
   
   if not(MST.has_node(fromNode)): #only add node to the graph/tree if it is not already in the graph/tree
      MST.add_node(fromNode)

   if not(MST.has_node(toNode)):  #only add node to the graph/tree if it is not already in the graph/tree
      MST.add_node(toNode)
      
   MST.add_edge(fromNode, toNode, weight = edgeWeight) #draw the edge bewteen the two nodes and add their weight
   does_add_edge_forms_a_cycle = isCycle(MST) #check if the newly added edge forms a cycle
   if does_add_edge_forms_a_cycle: #if true remove the edge
    MST.remove_edge(fromNode, toNode)
    mstValue = mstValue - edgeWeight #subtract the weight from the MST value

pos = nx.spring_layout(MST, seed=7)  # positions for all nodes - seed for reproducibility

# Draw nodes
nx.draw_networkx_nodes(MST, pos, node_size=700)

# Draw edges
nx.draw_networkx_edges(MST, pos, width=2, style="solid")

# Draw node labels
nx.draw_networkx_labels(MST, pos, font_size=14)

# Draw edge weight labels
edge_labels = nx.get_edge_attributes(MST, "weight")
nx.draw_networkx_edge_labels(MST, pos, edge_labels)

print("The MST Value is :", mstValue)
# Display the graph
mp.axis("off")  # Remove the rectangular box around the graph
mp.show()
