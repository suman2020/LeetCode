class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        #https://www.youtube.com/watch?v=EfkvVigVou0
        
        # Build the graph
        
        graph = collections.defaultdict(dict)
        
        for (x,y),val in zip(equations,values):
            
            graph[x][y] = val
            graph[y][x] = 1.0/val
        
        print(graph) #{'a': {'b': 2.0}, 'b': {'a': 0.5, 'c': 3.0}, 'c': {'b': 0.3333333333333333}})

        def dfs(x,y,visited):
            if x not in graph or y not in graph:
                return -1.0
            
            # direct connection: x,y
            if y in graph[x]:
                return graph[x][y]
                
            # no direct connection
            # iterate over all the nodes x is connected to
            
            for i in graph[x]:
                if i not in visited:
                    visited.add(i)
                    temp = dfs(i,y,visited)
                    if temp == -1:
                        continue
                    else:
                        return graph[x][i] * temp
                    
            return -1
            
        
        res = []
        # DFS function
        for query in queries:
            res.append(dfs(query[0],query[1], set()))
            
        return res
    
    
        # Time complecity: O(mn)-> n: no of input equations, m: no of queries