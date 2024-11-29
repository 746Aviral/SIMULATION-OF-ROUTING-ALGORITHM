def distance_vector_algorithm(graph):
    # Initialize routing tables (each node has a dictionary of costs to other nodes)
    routing_table = {node: {n: float('inf') for n in graph.nodes()} for node in graph.nodes()}
    for node in graph.nodes():
        routing_table[node][node] = 0  # Distance to itself is zero

    # Update routing table based on neighbors
    for _ in range(len(graph.nodes()) - 1):  # Bellman-Ford style iteration
        for u, v, data in graph.edges(data=True):
            weight = data['weight']
            for node in graph.nodes():
                if routing_table[u][node] > routing_table[v][node] + weight:
                    routing_table[u][node] = routing_table[v][node] + weight
                if routing_table[v][node] > routing_table[u][node] + weight:
                    routing_table[v][node] = routing_table[u][node] + weight

    return routing_table
