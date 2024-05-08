# %%
import matplotlib.pyplot as plt
import networkx as nx

# Define the cycle for reversing a linked list
cycle = {
    "next_node": "current.next",
    "current.next": "prev",
    "prev": "current",
    "current": "next_node",
}

# Create a directed graph
G = nx.DiGraph()

# Add edges to the graph based on the cycle
for start_node, end_node in cycle.items():
    G.add_edge(start_node, end_node)

# Define position for each node
pos = {
    "next_node": (0, 1),    # Top
    "current.next": (-1, 0),  # Left
    "prev": (0, -1),        # Bottom
    "current": (1, 0),      # Right
}
# Draw the graph again with the specified positions
# Draw the graph with specified positions and larger nodes and text
nx.draw(G, pos, with_labels=True, arrows=True, node_size=5000,
        node_color='skyblue', font_size=16, font_weight='bold', width=2)
plt.title("Cycle of Reversing a Linked List (Specified Layout)", fontsize=18)
plt.show()

# %%
