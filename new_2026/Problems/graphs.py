graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5],
    3: [1],
    4: [1, 5],
    5: [2, 4]
}

"""1) Given an adjacency list, print all nodes reachable from a starting node using BFS."""
from collections import deque
from math import dist
def bfs_adjacency(graph):
    q = deque()
    seen = set()

    source = 0
    seen.add(source)      # mark source as visited
    q.append(source)      # enqueue source

    while q:
        node = q.popleft()   # dequeue front node
        print(node)          # visit node
        for nei_node in graph[node]:       # check all neighbors
            if nei_node not in seen:       # only visit unvisited nodes
                seen.add(nei_node)         # mark as visited
                q.append(nei_node)         # enqueue neighbor

#bfs_adjacency(graph)

"""2) Given an adjacency list, print all nodes reachable from a starting node using DFS."""

def dfs_iterative(graph):
    seen = set()
    source = 0
    seen.add(source)
    stack = [source]

    while stack:
        node = stack.pop()
        print(node)
        for nei_node in graph[node]:
            if nei_node not in seen:
                seen.add(nei_node)
                stack.append(nei_node)

#dfs_iterative(graph)

"""3) Given a graph, detect if a cycle exists using DFS."""

def dfs_cycle(graph, node, seen, parent):
    seen.add(node)                        # mark current node as visited
    for nei_node in graph[node]:
        if nei_node not in seen:          # unvisited neighbor — recurse
            if dfs_cycle(graph, nei_node, seen, node):  # pass current as parent
                return True               # cycle found deeper in recursion
        elif nei_node != parent:          # visited and not parent — cycle found
            return True
    return False                          # no cycle from this node

seen = set()
(dfs_cycle(graph, 0, seen, -1))     # -1 = no parent for source node

"""4) Given a graph, check if it is bipartite (can be colored with 2 colors such that no adjacent nodes share the same color)."""

def check_bipartite(graph):
    color = {}                          # stores color (0 or 1) for each node
    for start in graph:
        if start not in color:          # handle disconnected components
            queue = deque([start])
            color[start] = 0            # assign first color to start node
            while queue:
                node = queue.popleft()
                for nei in graph[node]:
                    if nei not in color:             # unvisited neighbor
                        color[nei] = 1 - color[node] # assign opposite color
                        queue.append(nei)
                    elif color[nei] == color[node]:  # same color as current — conflict
                        return False
    return True                         # no conflicts — graph is bipartite

(check_bipartite(graph))

"""5) Given a graph, find the shortest path (by number of hops) between two nodes using BFS."""

def bfs_distance(graph, source, destination):
    distance = {}
    q = deque()
    seen = set()

    seen.add(source)             # mark source as visited
    q.append(source)             # enqueue source
    distance[source] = 0        # distance to source is 0

    while q:
        node = q.popleft()       # dequeue front node
        for nei_node in graph[node]:
            if nei_node not in seen:
                seen.add(nei_node)                          # mark as visited
                distance[nei_node] = distance[node] + 1    # one hop further than current
                q.append(nei_node)                          # enqueue neighbor

    return distance[destination]   # return shortest hop count to destination

print(bfs_distance(graph, 1, 4))