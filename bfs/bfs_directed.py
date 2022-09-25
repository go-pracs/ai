graph = {
        1:[5],
        2:[6,1],
        5:[4],
        6:[3],
        3:[2,7],
        4:[3],
        7:[]
}
visited = [] 
queue = []    

def bfs(visited, graph, node): 
  visited.append(node)
  queue.append(node)
  while queue:          
    m = queue.pop(0) 
    print (m) 
    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)
        
bfs(visited, graph, 3)
