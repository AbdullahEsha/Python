graph = {
    0 : [1,2],
    1 : [2],
    2 : [3],
    3 : [1,2]
}

visited = set() 

def dfs(visited, graph, node):
    if node not in visited:
        print (node)
        visited.add(node)
        for start in graph[node]:
            dfs(visited, graph, start)

# Driver Code
dfs(visited, graph, 0)