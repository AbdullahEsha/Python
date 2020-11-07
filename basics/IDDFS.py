from collections import defaultdict
 
class Graph:
 
    def __init__(self,vertices):
 
     
        self.V = vertices  
        self.graph = defaultdict(list)
 
    def addEdge(self,u,v):
        self.graph[u].append(v)
 

    def dls(self,src,target,maxDepth):
 
        if src == target : 
            return True
 
        if maxDepth <= 0 : 
            return False
 
        for i in self.graph[src]:
                if(self.dls(i,target,maxDepth-1)):
                    return True
        return False
 
     
    def iddfs(self,src, target, maxDepth):
 
        for i in range(maxDepth):
            if (self.dls(src, target, i)):
                return True
        return False
 

g = Graph (7);
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 3)
g.addEdge(1, 4)
g.addEdge(2, 5)
g.addEdge(2, 6)
 
target = 5; maxDepth = 10; src = 0
 
if g.iddfs(src, target, maxDepth) == True:
    print ("reachable target at: ",target)
else :
    print ("NOT reachable target at: ",target)