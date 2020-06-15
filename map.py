import util

#######################
# Map Functions       #
#######################

class NTU_MAP:
    """
    An NTU_Map object is a graph representation of (part of) the NTU Map.
    Our graph implentatation is a dictionary-based adjancency list.
    Keys are the nodes (i.e buildings, places) while values are lists of
    connected edge objects (i.e paths and their weights).
    
    vertex : [[edge object]]
    [edge object] = [destination vertex, weigght]
    
    Data structure inspired from ((https://www.python.org/doc/essays/graphs/)
    """
         
    # map = {'A': [['B', 1], ['D', 1]],                     # String representation of the map
    #        'B': [['A', 1], ['C', 1], ['E', 1]],           # (It's a 3 x 3 Grid)
    #        'C': [['B', 1], ['F', 1]],                     #
    #        'D': [['A', 1], ['E', 1], ['G', 1]],           # A - B - C
    #        'E': [['B', 1], ['D', 1], ['F', 1], ['H', 1]], # |   |   |
    #        'F': [['C', 1], ['E', 1], ['I', 1]],           # D - E - F
    #        'G': [['D', 1], ['H', 1]],                     # |   |   |
    #        'H': [['G', 1], ['E', 1], ['I', 1]],           # G - H - I
    #        'I': [['F', 1], ['H', 1]]
    # }
    
    map = {'CSIE-DerTian Hall': [['Barry Lam Hall', 1], ['Workshop of Mechanical Engineering', 1], ['EE Bldg. No. 2', 1], ['Dept. of Sociology / Dept. of Social Work', 1], ['Graduate Institute of Applied Mechanics', 1], ['College of Engineering Bldg.', 1]],
           'Barry Lam Hall': [['CSIE-DerTian Hall', 1], ['Workshop of Mechanical Engineering', 1], ['Graduate Institute of Journalism', 1], ['Tseng Jiang Hall', 2], ['EE Bldg. No. 2', 1]],
           'Workshop of Mechanical Engineering': [['Barry Lam Hall', 1], ['CSIE-DerTian Hall', 1], ['Graduate Institute of Journalism', 1], ['College of Social Sciences Bldg.', 1]],
           'Graduate Institute of Journalism': [['Barry Lam Hall', 1], ['Workshop of Mechanical Engineering', 1], ['Graduate Institute of National Development', 1], ['Tseng Jiang Hall', 1]],
           'EE Bldg. No. 2': [['Barry Lam Hall', 1], ['CSIE-DerTian Hall', 1], ['Tseng Jiang Hall', 1], ['College of Engineering Bldg.', 1]], 
           'Tseng Jiang Hall': [['Barry Lam Hall', 2], ['EE Bldg. No. 2', 1], ['Graduate Institute of Journalism', 1]],
           'Dept. of Sociology / Dept. of Social Work': [['CSIE-DerTian Hall', 1], ['College of Social Sciences Bldg.', 1], ['Graduate Institute of National Development', 2], ['Foreign Language Teaching and Resource Center', 1]],
           'Graduate Institute of National Development': [['Dept. of Sociology / Dept. of Social Work', 2], ['Graduate Institute of Journalism', 1], ['College of Social Sciences Bldg.', 1]],
           'College of Social Sciences Bldg.': [['Graduate Institute of National Development', 1], ['Dept. of Sociology / Dept. of Social Work', 1], ['Workshop of Mechanical Engineering', 1]],
           
           'Language Bldg.': [['Foreign Language Teaching and Resource Center', 0], ['Computer and Information Networking Center', 1]],
           'Foreign Language Teaching and Resource Center': [['Language Bldg.', 0], ['Graduate Institute of Applied Mechanics', 1], ['Dept. of Sociology / Dept. of Social Work', 1], ['Dept. of Psychology (North Hall)', 1], ['Computer and Information Networking Center', 1], ['Fisheries Science Research Bldg.', 1]],
           'Computer and Information Networking Center': [['Language Bldg.', 1], ['Foreign Language Teaching and Resource Center', 1], ['Fisheries Science Research Bldg.', 1]],
           'Fisheries Science Research Bldg.': [['Computer and Information Networking Center', 1], ['8th Women`s Dorm', 1], ['Foreign Language Teaching and Resource Center', 1]],
           'Graduate Institute of Applied Mechanics': [['Foreign Language Teaching and Resource Center', 1], ['Dept. of Psychology (North Hall)', 1], ['Dept. of Psychology (South Hall)', 1], ['CSIE-DerTian Hall', 1]],
           'Dept. of Psychology (North Hall)': [['Graduate Institute of Applied Mechanics', 1], ['Foreign Language Teaching and Resource Center', 1], ['Dept. of Psychology (South Hall)', 1], ['8th Women`s Dorm', 1]],
           'Dept. of Psychology (South Hall)': [['Graduate Institute of Applied Mechanics', 1], ['Dept. of Psychology (North Hall)', 1], ['College of Engineering Bldg.', 1], ['9th Women`s Dorm', 1]],  
           '9th Women`s Dorm': [['Dept. of Psychology (South Hall)', 1], ['8th Women`s Dorm', 1]],
           '8th Women`s Dorm': [['Dept. of Psychology (North Hall)', 1], ['9th Women`s Dorm', 1], ['Fisheries Science Research Bldg.', 1]],
           'College of Engineering Bldg.': [['Dept. of Psychology (South Hall)', 1], ['CSIE-DerTian Hall', 1], ['EE Bldg. No. 2', 1]]
    }
    
    def getMap(self):
      return self.map
      
def aStarSearch(map, start, end):
    """
    A* Search finds the path of lowest combined cost between a
    start vertex and end vertex.
    """
    
    path = []     # list moves to a given node
    cost = 0      # cost of reaching a given node
    node = ()     # (position of, path to, cost to) current node
    visited = []  # list of visited nodes
    
    # A* implementation
    # Begin py pushing start node into frontier (Priority Queue)
    frontier = util.PriorityQueue()
    priority = cost # + heuristic (might not need this)
    frontier.push((start, path, cost), priority)

    # Explore the graph in search of the goal state
    while not frontier.isEmpty():
        # Examine the current node
        position, path, cost = frontier.pop()
        # If position is goal state, return its path
        if position == end:
            return path
        # If current node not visited add it to list
        if position not in visited:
            visited.append(position)
            # Insert any child nodes into frontier
            for child, weight in map[position]:
                childCost = cost + weight
                priority = childCost # + heuristic (might not need this)
                frontier.push((child, path + [child], childCost), priority)
    
    return [] # goal state not found, no solution set


map = NTU_MAP().getMap()

print(aStarSearch(map, 'Fisheries Science Research Bldg.', 'Tseng Jiang Hall'))

# Reasearch Rochio Relevance Feedback
