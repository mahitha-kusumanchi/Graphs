from heapq import heappop
from heapq import heappush
from collections import deque
class graphs:
    def __init__(self,n):
        self.n=n
        self.adjList=[]
        for i in range(self.n):
            self.adjList.append([])
    def addEdge(self,vertex1,vertex2,weight):
        self.adjList[vertex1].append([vertex2,weight])
        self.adjList[vertex2].append([vertex1,weight])
    def bfs(self):
        result=[]
        visited=[0]*self.n
        queue=deque([0])
        visited[0]=1
        while queue:
            vertex=queue.popleft()
            result.append(vertex)
            for neighbor ,weight in self.adjList[vertex]:
                if visited[neighbor]==0:
                    visited[neighbor]=1
                    queue.append(neighbor)
        return result
    def dfs(self):
        result=[]
        visited=[0]*self.n
        visited[0]=1
        result.append(0)
        self._dfs(result,0,visited)
        return result
    def _dfs(self,result,node,visited):
        for neighbor,weight in self.adjList[node]:
            if visited[neighbor]==0:
                result.append(neighbor)
                visited[neighbor]=1
                self._dfs(result, neighbor, visited)
    def dijkstra(self):
        dist=[float('inf')]*self.n
        dist[0]=0
        pq=[(0,0)]
        while pq:
            u,current_distance=heappop(pq)
            for neighbor,distance in self.adjList[u]:
                if dist[neighbor]>current_distance+distance:
                    dist[neighbor]=current_distance+distance
                    heappush(pq,(neighbor,current_distance+distance))
        return dist
g=graphs(6)
g.addEdge(0,1,2)
g.addEdge(0,3,4)
g.addEdge(4,2,5)
g.addEdge(1,2,7)
g.addEdge(2,3,1)
g.addEdge(3,5,3)
print(g.bfs())
print(g.dfs())
print(g.dijkstra())
