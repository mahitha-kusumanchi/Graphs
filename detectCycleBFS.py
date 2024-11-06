from collections import deque
def detect(src,visited,arr):
    q=deque([(src,-1)])
    visited[src]=1
    while q:
        node,parent=q.popleft()
        for neighbor in arr[node]:
            if visited[neighbor]==0:
                visited[neighbor]=1
                q.append((neighbor,node))
            elif(parent!=neighbor):
                return True
    return False
def detectCycle(arr):
    visited=[0]*len(arr)
    for i in range(len(arr)):
        if visited[i]==0:
            if detect(i,visited,arr):
                return True
    return False
adj = [[], [2,3], [1,3], [2,1]]
print(detectCycle(adj))
