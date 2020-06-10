
# The NTU Map is represented by a graph
# The graph is based on lists and dictionaries
# where the keys of the dictionarie are the nodes
# and the values are lists of connected nodes
# data structure inspired from (https://www.python.org/doc/essays/graphs/)
map = {'A': ['B', 'D'],
       'B': ['A', 'C', 'E'],
       'C': ['B', 'F'],
       'D': ['A', 'E', 'G'],
       'E': ['B', 'D', 'F', 'H'],
       'F': ['C', 'E', 'I'],
       'G': ['D', 'H'],
       'H': ['G', 'E', 'I'],
       'I': ['F', 'H']
}
        
"""
String representation of the map
(It's a 3 x 3 Grid)

A - B - C
|   |   |
D - E - F
|   |   |
G - H - I
"""

def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not start in graph:
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath: return newpath
    return None
    
print(find_path(map, 'A', 'I'))