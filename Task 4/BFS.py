from collections import deque

# The graph to be Traversed
graph = {
    'A': ['B','C'],
    'B': ['D','E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# BFS Functions
def bfs(graph, start, goal):
    #Queue for sorting nodes to visit
    queue = deque([start])
    visited = []
    #dictionary to store parent of each node
    parent= {}
    parent [start] = None
    print(" ====== Breadth First search Traversal===")

    #Continue while queue is not empty
    while queue:
        #Remove first node from queue
        current = queue.popleft()

        #visit node if not already visited
        if current not in visited:
            print("visited node :", current)
            visited.append(current)

            #Goal test
            if current == goal:
                print("\n Goal Found")
                break
            #Adding neighbours to the queue
            for neighbour in graph[current]:
                #Avoiding duplicate visits
                if neighbour not in visited:
                    queue.append(neighbour)
                    parent[neighbour] = current

#Reconstructing shortest path
    path= []

    node = goal

    while node is not None:
        node = parent[node]

#Reverse path to start goal
    path.reverse()
    print("\n =====Shortest Path ")
    print("->".join(path))

start_node = 'A'
goal_node = 'F'

bfs(graph, start_node, goal_node)
