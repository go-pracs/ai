from queue import PriorityQueue
v = 14
graph = [[] for i in range(v)]
def addedge(x, y, cost):
	graph[x].append((y, cost))
	graph[y].append((x, cost))
addedge(0, 1, 3)
addedge(0, 2, 6)
addedge(0, 3, 5)
addedge(1, 4, 9)
addedge(1, 5, 8)
addedge(2, 6, 12)
addedge(2, 7, 14)
addedge(3, 8, 7)
addedge(8, 9, 5)
addedge(8, 10, 6)
addedge(9, 11, 1)
addedge(9, 12, 10)
addedge(9, 13, 2)
source = 0
target = 9

def print_details(pq,visited):
    print("closed",end=" ")
    for idx,i in enumerate(visited):
        if i==True:
            print(idx, end=" ")
    print("\nopen",end=" ")
    for idx,i in enumerate(visited):
        if i==False:
            print(idx, end=" ")
    print("\npriority Queue",end=" ")
    temp=[]
    for i in range(len(pq.queue)):
        temp.append(pq.queue[i])
    temp.sort(key=lambda pair: pair[0])
    print(temp,"\n")

def best_first_search(source,target,n):
    print("Priority Queue ('cost','node')")
    visited=[False]* n
    pq=PriorityQueue()
    visited[source]=True
    pq.put((0,source))
    while pq.empty()==False:
        
        print_details(pq,visited)
        u=pq.get()[1]
        print("Current best Node ",u)
        if u==target:
            print("Goal node found!!") 
            break
        for v,c in graph[u]:
            if visited[v]==False:
                visited[v]=True
                pq.put((c,v))


best_first_search(source, target, v)