# Define the graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Initialize a set to keep track of visited nodes
visited = set()

def dfs(graph, node):
    # Mark the node as visited
    visited.add(node)
    
    # Process the node (e.g., print it)
    print(node)
    
    # Recursively visit all the neighbors
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor)

# Start DFS from a given node (e.g., 'A')
dfs(graph, 'A')
