from heapq import heappop
from heapq import heappush
def dijkstra(adj):
    V=len(adj)
    dist=[float('inf')]*V
    dist[0]=0
    pq=[(0,0)]
    while pq:
        distance,node=heappop(pq)
        for neighbor,weight in adj[node]:
            if dist[neighbor]>weight+distance:
                dist[neighbor]=weight+distance
                heappush(pq,(dist[neighbor],neighbor))
    return dist
V = 6
E = 7
edge = [[0,1,2],[0,4,1],[4,5,4],[4,2,2],[1,2,3],[2,3,6],[5,3,1]]
adj=[[] for i in range(V)]
for arr in edge:
    adj[arr[0]].append((arr[1],arr[2]))
    adj[arr[1]].append((arr[0],arr[2]))
print(dijkstra(adj))
