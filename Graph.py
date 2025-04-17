import matplotlib.pyplot as plt  # SECOND
import networkx as nx  # SECOND

count_edges = 0  # SECOND

# Function to insert edges based on user input
def insert():  # BASE
    V = int(input("Enter the number of vertices: "))
    adj = [[] for _ in range(V)]

    print("Enter the edges (e.g., 'u v' to connect u to v, or type 'done' to finish):")
    while True:
        edge = input()
        if edge.lower() == "done":
            break
        try:
            u, v = map(int, edge.split())
            if 0 <= u < V and 0 <= v < V:
                adj[u].append(v)
            else:
                print(f"Invalid edge ({u}, {v}): vertices must be between 0 and {V - 1}.")
        except ValueError:
            print("Invalid input. Please enter edges in the format 'u v'.")

    return adj, V


# Function to display adjacency list
def showList(adj, V):  # BASE
    print("Adjacency List:")
    for i in range(V):
        print(i, end='')
        for j in adj[i]:
            print(' --> ' + str(j), end='')
        print()
    print()


# Function to convert adjacency list to adjacency matrix
def convert(adj, V):  # FIRST
    matrix = [[0 for _ in range(V)] for _ in range(V)]
    for i in range(V):
        for j in adj[i]:
            matrix[i][j] = 1
    return matrix


# Function to display adjacency matrix
def showMatrix(matrix, V):  # FIRST
    print("Adjacency Matrix:")
    for i in range(V):
        for j in range(V):
            print(matrix[i][j], end=' ')
        print()
    print()


# Function to visualize a graph using the adjacency list
def drawandcount(adj, V):  # SECOND
    global count_edges  # Use the global count_edges variable
    G = nx.DiGraph() #creates the directed graph object
    for i in range(V):
        for j in adj[i]:
            G.add_edge(i, j) #add edge
            count_edges += 1  # Increment count_edges

    nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray',
            font_weight='bold', node_size=1000) #draws the graph
    plt.title("Graph Visualization")
    plt.show()


# Driver code
# real implementation
if __name__ == '__main__':
    # Insert edges based on user input
    adjList, V = insert()  # BASE

    # Display adjacency list
    showList(adjList, V)  # BASE

    # Convert adjacency list to adjacency matrix
    adjMatrix = convert(adjList, V)  # FIRST

    # Display adjacency matrix
    showMatrix(adjMatrix, V)  # FIRST

    # Visualize the graph directly from the adjacency matrix
    drawandcount(adjList, V)  # SECOND

    print("Number of connections (edges) =", count_edges)

