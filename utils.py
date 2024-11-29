import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import json
import random

# Create graph manually if no file is provided
def create_graph():
    G = nx.Graph()
    nodes = [1, 2, 3, 4, 5]
    G.add_nodes_from(nodes)
    edges = [(1, 2, 4), (1, 3, 2), (2, 3, 1), (2, 4, 5), (3, 4, 8), (4, 5, 6)]
    G.add_weighted_edges_from(edges)
    return G

# Visualize routing table for each algorithm
def visualize_routing_table(graph, routing_table, algorithm_name):
    pos = nx.spring_layout(graph)
    plt.figure()
    nx.draw(graph, pos, with_labels=True, node_size=700, node_color='lightgreen')
    labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)

    for node, table in routing_table.items():
        print(f"{algorithm_name} - Node {node}: {table}")
    
    plt.title(f"{algorithm_name} Routing Visualization")
    plt.show()

# Load graph from CSV file
def load_graph_from_csv(file_path):
    G = nx.Graph()
    data = pd.read_csv(file_path)
    for _, row in data.iterrows():
        G.add_edge(row['node1'], row['node2'], weight=row['weight'])
    return G

# Load graph from JSON file
def load_graph_from_json(file_path):
    G = nx.Graph()
    with open(file_path) as f:
        data = json.load(f)
        for edge in data['edges']:
            G.add_edge(edge['node1'], edge['node2'], weight=edge['weight'])
    return G

# Simulate link failure by removing a random edge
def simulate_link_failure(graph):
    if len(graph.edges) > 0:
        edge = random.choice(list(graph.edges))
        print(f"Simulating link failure on edge: {edge}")
        graph.remove_edge(*edge)
        return edge
    else:
        print("No edges left to remove.")
        return None
