from queue import PriorityQueue
import json

with open('Assignment1.3Graph.json') as f:
    data = json.load(f)

#       a
#      /|\
#     b e c
#   /| /  |
#  d f    g

#Start and Goal of our Searches  
start = 'a'
goal = 'g'

#Creating our Adjacent List for each Node.
# def setup_graph(data):
#     graph = {}
#     for node in data['nodes']:
#         grouping = {"neighbor":"allowance"}
#         for edge in data['edges']:
#             if edge['source'] == node:
#                 grouping["neighbor"] = edge['target']
#                 grouping["allowance"]= edge['cost']
#                 grouping.update()

#             if edge['target'] == node:
#                 grouping["neighbor"] = edge['target']
#                 grouping["allowance"]= edge['cost']
#                 grouping.update()
#         graph.update({node:grouping})
#     print(graph)
#     return graph

def setup_graph(data):
    graph = {}
    for node in data['nodes']:
        grouping={} 
        for edge in data['edges']:
            if edge['source'] == node:
             grouping.update({edge['target']:edge['cost' ]} )
        graph.update({node:grouping})
    return graph
setup_graph(data) 
adjList = setup_graph(data)

#Using Priority Queue to try and implement uniform cost search
def UCS(adjList,start,goal):
     #Creating arrays, queues, sets
    queue = PriorityQueue()
    visited = {}
    level = {}
    parent = {}
    bfs_traversal = []
    path = []
    
     #Initializing our arrays
    for node in adjList.keys():
        visited[node] = False
        parent[node] = None
        level[node] = -1 
        
    visited[start] = True #Initialize our start node as visited
    level[start] = 0 #Initializes our source node level as 0
    queue.put(start) #putting our start node into the queue
    
    #LIFO of queue into our bfs_traversal
    while not queue.empty():
        x = queue.get() #Remove item from queue
        bfs_traversal.append(x) #Adds item last item we got from queue into traversal
        print(bfs_traversal)
        
        for AI in adjList[x]:
            if not visited[AI]:
                visited[AI] = True #Add to Visited
                parent[AI] = x
                level[AI] = level[x] + 1 #Increases level
                queue.put(AI) #Put item on queue
                
    #Create our Shortest Path from Start to Goal
    while goal is not None:
        path.append(goal)
        goal = parent[goal]
    path.reverse() #Reverse our path
    print(path) #Bingo
    
UCS(adjList,start,goal)
