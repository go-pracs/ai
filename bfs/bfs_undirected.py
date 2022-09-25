graph = {
    1:[2,5],
    2:[6,3,5,1],
    5:[1,2,4],
    6:[3,2],
    3:[7,4,6,2],
    4:[5,3],
    7:[3]
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