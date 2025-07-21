import numpy as np
from collections import deque
class Graph:
    def __init__(self, size):
        self.size = size
        self.adj_list = [[0]*size for _ in range(size)]
        self.vertex_data = [''] * size

    def addEdge(self,u,v):
        if 0 <= u < self.size and 0 <= v < self.size :
            self.adj_list[u][v]= 1

    def addVertexData(self,vertex,data):
        if 0<= vertex < self.size:
            self.vertex_data[vertex] = data
        
    def print_nodes(self):
        print('Adjancy Matrix : ')
        for row in self.adj_list:
            print(row)
        for index,data in enumerate(self.vertex_data):
            print(f"node {index} --> Data {data}")

    def dfs_iterative_adj_matrix(self, start_node):
        """
    Performs an iterative Depth-First Search (DFS) on a graph represented
    by an adjacency matrix.

    Args:
        graph_matrix (list of lists): The adjacency matrix where graph_matrix[i][j]
                                      is 1 if there's an edge from i to j, else 0.
        start_node (int): The starting node for the DFS traversal.

    Returns:
        list: A list of nodes in the order they were visited during the DFS.
    """
        num_nodes = len(self.adj_list)
        visited = [False] * num_nodes  # Keep track of visited nodes
        stack = [start_node]  # Stack for DFS traversal
        traversal_order = []  # To store the order of visited nodes

        while stack:
            current_node = stack.pop()

            if not visited[current_node]:
                visited[current_node] = True
                traversal_order.append(current_node)

            # Explore neighbors of the current_node
            # Iterate in reverse order to ensure lower-indexed neighbors are
            # processed first (if multiple unvisited neighbors exist),
            # mimicking recursive DFS behavior where adjacent nodes are
            # pushed onto the stack in a specific order.
                for neighbor in range(num_nodes - 1, -1, -1):
                    if self.adj_list[current_node][neighbor] == 1 and not visited[neighbor]:
                        stack.append(neighbor)

        return traversal_order

    

    def bfs_adjacency_matrix(self, start_node):
        """
    Performs a Breadth-First Search (BFS) on a self.adj_list represented by an adjacency matrix.

    Args:
        self.adj_list (list of list of int): The adjacency matrix where self.adj_list[i][j] == 1
                                     indicates an edge from node i to node j.
        start_node (int): The starting node for the BFS traversal.

    Returns:
        list: A list containing the order of visited nodes during the BFS traversal.
    """
        num_nodes = len(self.adj_list)
        visited = [False] * num_nodes  # Keep track of visited nodes
        queue = deque()               # Queue for BFS traversal

    # Mark the start node as visited and enqueue it
        visited[start_node] = True
        queue.append(start_node)
    
        traversal_order = []

        while queue:
            current_node = queue.popleft()  # Dequeue a node
            traversal_order.append(current_node) # Add to traversal order

        # Explore neighbors of the current node
            for neighbor in range(num_nodes):
            # Check if there's an edge and the neighbor hasn't been visited
                if self.adj_list[current_node][neighbor] == 1 and not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
                
        return traversal_order


graph = Graph(6)
visited = [False] * 6
graph.addVertexData(0,'A')
graph.addVertexData(1,'B')
graph.addVertexData(2,'C')
graph.addVertexData(3,'D')
graph.addVertexData(4,'E')
graph.addVertexData(5,'F')
graph.addEdge(0,1)
graph.addEdge(1,0)
graph.addEdge(0,2)
graph.addEdge(0,3)
graph.addEdge(2,3)
graph.addEdge(2,5)

graph.addEdge(1,5)
graph.addEdge(3,0)

graph.addEdge(4,1)
graph.addEdge(4,5)

graph.print_nodes()

print(graph.dfs_iterative_adj_matrix(0))
print(graph.bfs_adjacency_matrix(0))