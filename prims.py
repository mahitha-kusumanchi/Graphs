
import heapq
def spanningTree(adj):
    minHeap=[(0,0,-1)]
    V=len(adj)
    vis=[0]*V
    mstWt=0
    mstEdges=[]
    edgesInMst=0
    while minHeap and edgesInMst<V:
        weight,u,parent=heapq.heappop(minHeap)
        if parent!=-1:
            mstEdges.append((u,parent))
        if vis[u]:
            continue
        mstWt+=weight
        vis[u]=1
        edgesInMst+=1
        for v,w in adj[u]:
            if vis[v]==0:
                heapq.heappush(minHeap,(w,v,u))
    print(mstEdges)
    print(mstWt)
'''adj = [
    [(1, 5), (2, 1)],  # Node 0 is connected to Node 1 (weight 5) and Node 2 (weight 1)
    [(0, 5), (2, 3)],  # Node 1 is connected to Node 0 (weight 5) and Node 2 (weight 3)
    [(0, 1), (1, 3)]   # Node 2 is connected to Node 0 (weight 1) and Node 1 (weight 3)
]
adj = [
    [(1, 2)],      # Node 0 is connected to Node 1 (weight 2)
    [(0, 2)],      # Node 1 is connected to Node 0 (weight 2)
    []             # Node 2 is disconnected
]
adj = [[]]  # Only one node with no edges
# Expected MST edges: []
# Expected MST weight: 0

adj = [
    [(1, 1)],      # Node 0 is connected to Node 1 (weight 1)
    [(0, 1), (2, 2)], # Node 1 is connected to Node 0 (weight 1) and Node 2 (weight 2)
    [(1, 2), (3, 3)], # Node 2 is connected to Node 1 (weight 2) and Node 3 (weight 3)
    [(2, 3)]        # Node 3 is connected to Node 2 (weight 3)
]
# Expected MST edges: [(0, 1), (1, 2), (2, 3)]
# Expected MST weight: 6
'''
adj = [
    [(1, 1), (2, 4), (3, 3)],  # Node 0 connected to Node 1 (weight 1), Node 2 (weight 4), Node 3 (weight 3)
    [(0, 1), (2, 2), (3, 5)],  # Node 1 connected to Node 0 (weight 1), Node 2 (weight 2), Node 3 (weight 5)
    [(0, 4), (1, 2), (3, 1)],  # Node 2 connected to Node 0 (weight 4), Node 1 (weight 2), Node 3 (weight 1)
    [(0, 3), (1, 5), (2, 1)]   # Node 3 connected to Node 0 (weight 3), Node 1 (weight 5), Node 2 (weight 1)
]
#[(1, 0), (2, 1), (3, 2)]
#4
# Expected MST edges may vary, but MST weight should be the minimum possible, e.g., 4
spanningTree(adj)
