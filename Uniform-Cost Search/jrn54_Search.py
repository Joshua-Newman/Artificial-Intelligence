

from queue import LifoQueue
from queue import PriorityQueue
from queue import Queue
import json

with open('Assignment1Graph.json') as f:
    data = json.load(f)

with open('Assignment1.3Graph.json') as f:
    data1 = json.load(f)

#       a
#      /|\
#     b e c
#   /| /  |
#  d f    g

#Start and Goal of our Searches  
start = 'a'
goal = 'g'

#Creating our Adjacent List for each Node.
def setup_graph(data):
    graph = {}
    for node in data['nodes']:
        neighbors = set()
        for edge in data['edges']:
            if edge['source'] == node:
                neighbors.add(edge['target'])
            if edge['target'] == node:
                neighbors.add(edge['source'])
        graph.update({node: neighbors})
    return graph
adjList = setup_graph(data)

def setup_graph(data1):
    graph = {}
    for node in data1['nodes']:
        grouping={} 
        for edge in data1['edges']:
            if edge['source'] == node:
             grouping.update({edge['target']:edge['cost' ]} )
        graph.update({node:grouping})
    return graph
setup_graph(data1) 
adjList1 = setup_graph(data1)

#Depth-First Search.
def dfs(adjList, start, goal):
    #Creating arrays, queues, sets
    queue = LifoQueue()
    visited = {}
    level = {}
    parent = {}
    dfs_traversal = []
    path = []
    
    #Initializing our arrays
    for node in adjList.keys():
        visited[node] = False
        parent[node] = None
        level[node] = -1 
        
    visited[start] = True #Initialize our start node as visited
    level[start] = 0 #Initializes our source node level as 0
    queue.put(start) #putting our start node into the queue
    
    #FIFO of queue into our bfs_traversal
    while not queue.empty():
        x = queue.get() #Remove item from queue
        dfs_traversal.append(x) #Adds item last item we got from queue into traversal
        
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
    print("Our DFS path is: ",path) #Bingo
    
#Breadth-First Search.
def bfs(adjList, start, goal):
    #Creating arrays, queues, sets
    queue = Queue()
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
    print("Our BFS Path is: ",path) #Bingo
 
#Using Priority Queue to try and implement uniform cost search
def UCS(adjList1,start,goal):
     #Creating arrays, queues, sets
    queue = PriorityQueue()
    visited = {}
    level = {}
    parent = {}
    ucs_traversal = []
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
        ucs_traversal.append(x) #Adds item last item we got from queue into traversal
        # print(bfs_traversal) #Debugging to try and watch our traversal. 
        
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
    print("Our UCS Path is: ",path) #Bingo
 
dfs(adjList,start,goal)    
bfs(adjList,start,goal)
UCS(adjList1,start,goal)
    



