from distance_vector import distance_vector_algorithm
from link_state import link_state_algorithm
from utils import create_graph, visualize_routing_table, simulate_link_failure, load_graph_from_csv, load_graph_from_json

def main():
    # Load network graph from file or create manually
    file_type = input("Enter file type to load network (csv/json/none for manual): ").strip().lower()
    if file_type == "csv":
        file_path = input("Enter CSV file path: ").strip()
        G = load_graph_from_csv(file_path)
    elif file_type == "json":
        file_path = input("Enter JSON file path: ").strip()
        G = load_graph_from_json(file_path)
    else:
        # Create the network graph manually if no file is provided
        G = create_graph()
    
    # Run Distance Vector Algorithm
    print("Running Distance Vector Algorithm...")
    distance_vector_routing = distance_vector_algorithm(G)
    print("Distance Vector Routing Tables:")
    for node, table in distance_vector_routing.items():
        print(f"Node {node}: {table}")
    visualize_routing_table(G, distance_vector_routing, "Distance Vector")

    # Run Link State Algorithm
    print("\nRunning Link State Algorithm...")
    link_state_routing = link_state_algorithm(G)
    print("Link State Routing Tables:")
    for node, table in link_state_routing.items():
        print(f"Node {node}: {table}")
    visualize_routing_table(G, link_state_routing, "Link State")

    # Simulate link failures and recalculate routes
    while True:
        simulate = input("\nDo you want to simulate a link failure? (yes/no): ").strip().lower()
        if simulate == "yes":
            failed_edge = simulate_link_failure(G)
            if failed_edge:
                print("\nRecalculating routes after link failure...")
                distance_vector_routing = distance_vector_algorithm(G)
                link_state_routing = link_state_algorithm(G)
                visualize_routing_table(G, distance_vector_routing, "Distance Vector after failure")
                visualize_routing_table(G, link_state_routing, "Link State after failure")
        else:
            break

if __name__ == "__main__":
    main()
