graph = {
   1:[2,3],
   2:[4],
   3:[],
   4:[5],
   5:[],
   6:[4],

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