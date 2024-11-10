class disJoinSet:
    def __init__(self,V):
        self.parent=[i for i in range(V+1)]
        self.size=[0]*(V+1)
        self.rank=[0]*(V+1)
    def find(self,u):
        if self.parent[u]==u:
            return u
        self.parent[u]=self.find(self.parent[u])
        return self.parent[u]
    def unionBySize(self,u,v):
        root_u=self.find(u)
        root_v=self.find(v)
        if root_u!=root_v:
            if self.size[root_v]<self.size[root_u]:
                self.parent[root_v]=root_u
                self.size[root_u]+=self.size[root_v]
            else :
                self.parent[root_u] = root_v
                self.size[root_v] += self.size[root_u]
    def unionByRank(self,u,v):
        root_u=self.find(u)
        root_v=self.find(v)
        if root_u!=root_v:
            if self.rank[root_u]>self.rank[root_v]:
                self.parent[root_v]=root_u
            elif self.rank[root_u]<self.rank[root_v]:
                self.parent[root_u]=root_v
            else :
                self.parent[root_u]=root_v
                self.rank[root_v]+=1
def spanningTree(adj,V):
    edges=[]
    ds=disJoinSet(V)
    for i in range(V):
        for neighbor,weight in adj[i]:
            edges.append((weight,i,neighbor))
    edges.sort()
    result=[]
    mst_weight=0
    for w,u,v in edges :
        if ds.find(u)!=ds.find(v):
            mst_weight+=w
            ds.unionBySize(u,v)
            result.append([u,v])
    print(result)
    return mst_weight
V = 5
edges = [[0, 1, 2], [0, 2, 1], [1, 2, 1], [2, 3, 2], [3, 4, 1], [4, 2, 2]]
adj = [[] for _ in range(V)]
for u, v, w in edges:
    adj[u].append((v, w))
    adj[v].append((u, w))
mst_weight = spanningTree(adj,V)
print("The sum of all the edge weights:", mst_weight)
