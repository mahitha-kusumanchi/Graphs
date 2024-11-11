class Solution:
    def dfs(self,vis,st,node,adj):
        vis[node]=1
        for neighbor in adj[node]:
            if vis[neighbor]==0:
                self.dfs(vis,st,neighbor,adj)
        st.append(node)
    def toposort(self,V,adj):
        vis=[0]*V
        st=[]
        for i in range(V):
            if vis[i]==0:
                self.dfs(vis,st,i,adj)
        return st[::-1]
adj = [[], [3], [3], [], [0,1], [0,2]]
s=Solution()
result=s.toposort(6,adj)
print(result)
