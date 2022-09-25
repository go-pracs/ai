graph = {
   'A': ['B','C','E'],
    'B': ['D','F','A'],
    'C': ['G','A'],
    'D': ['B'],
    'E': ['F','A'],
    'F': ['E','B'],
    'G': ['C']
}
visited = set() # Set to keep track of visited nodes of the graph.
def dfs( graph, node, visited):  
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(graph, neighbour, visited)
# Driver Code
print("Following is the Depth-First Search")
dfs(graph, 'A', visited)