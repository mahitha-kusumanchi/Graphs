from collections import deque
def countProvinces(Arr):
    visited=[0]*len(Arr)
    count=0
    def dfs(index):
        q = deque([index])
        while q:
            temp = q.popleft()
            for a in Arr[temp] :
                if visited[a]==0:
                    q.append(a)
                    visited[a]=1
    for i in range(len(Arr)):
        if visited[i]==0:
            count+=1
            dfs(i)
    return count
adj = [[1,2],[0],[0]]
print(countProvinces(adj))
