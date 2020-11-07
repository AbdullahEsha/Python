from queue import PriorityQueue

def ucs_weight(from_node, to_node, weights):
    return weights.get((from_node, to_node), weights) if weights else 1


def ucs(graph, start, end, weights):
    frontier = PriorityQueue()
    frontier.put((0, start))
    explored = []

    while True:
        u,current_node = frontier.get()
        if current_node not in explored:
            explored.append(current_node)

        if current_node == end:
            print(explored)
            return
        

        for node in (graph[current_node]):
            if node not in explored:
                frontier.put((
                    u + ucs_weight(current_node, node, weights),
                    node
                ))

graph={
        'A': ['B','G','J'],
        'B': ['A','D'],
        'C': ['H'],
        'D': ['B','H','J'],
        'E': ['F','G','I'],
        'F': ['E','G','H','I'],
        'G': ['A','E','F','J'],
        'H': ['C','D','F','I'],
        'I': ['E','F','H'],
        'J': ['A','D','G']
    }
path_weight = {
        ('A', 'B'): 3,
        ('A', 'J'): 4,
        ('A', 'G'): 1,

        ('B', 'A'): 3,
        ('B', 'D'): 10,
        ('C', 'H'): 3,
        
        ('D', 'B'): 10,
        ('D', 'J'): 3,
        ('D', 'H'): 11,
        
        ('E', 'F'): 2,
        ('E', 'G'): 14,
        ('E', 'I'): 1,
        
        ('F', 'E'): 2,
        ('F', 'G'): 8,
        ('F', 'H'): 4,
        ('F', 'I'): 2,
        
        ('G', 'A'): 1,
        ('G', 'E'): 14,
        ('G', 'F'): 8,
        ('G', 'J'): 6,
        
        ('H', 'C'): 3,
        ('H', 'D'): 11,
        ('H', 'F'): 4,
        ('H', 'I'): 6,
        
        ('I', 'E'): 1,
        ('I', 'F'): 2,
        ('I', 'H'): 6,
        
        ('J', 'A'): 4,
        ('J', 'D'): 3,
        ('J', 'G'): 6
    }

ucs(graph,'A', 'C', path_weight)
