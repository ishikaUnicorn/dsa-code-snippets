class Graphs:
    def caller():
        #build adj_list
        vis=[0]*n
        self.dfs(----)
    def dfs(root,adj_list,ans,temp,vis):
        #some base case to ensure we add temp to and and return
        if vis[root]==1: return
        vis[root]=1
        lst=adj_list[root]
        for node in lst:
            #process node to see if it gets added to temp
            self.dfs(node,adj_list,ans,temp,vis)
        return
    def bfs(root,adj_list):
        q=deque()
        q.append(root)
        vis=[0]*n
        vis[root]=1
        while q:
            node=q.popleft()
            #process node and add neighbors from adj_list as needed
            #into q and ensure to add whatever needed to ans after popping
            for nei in adj_list[node]:
                if vis[nei]==1:continue
                q.append(nei)
                vis[nei]=1
    def cycle_detection_undirected(node,adj_list,parent,vis):
        if vis[node]==1:return False
        vis[node]=1
        for nei in adj_list[node]:
            if vis[nei]==1 and nei==parent:continue
            if vis[nei]==1:return True #cycle exists
            temp=self.cycle_detection_undirected(nei,adj_list,node,vis)
            if temp:return True
        return False
    def cycle_detection_directed(self,node,adj_list,vis):
        if vis[node]==2:return False
        vis[node]=1 #processing
        for nei in adj_list[node]:
            if vis[nei]==1:return True #cycle detected 
            if vis[nei]==2:continue
            temp=self.cycle_detection_directed(nei,adj_list,vis)
            if temp:return temp
        vis[node]=2
        return False
    def topo_kahns(courses,n):
        adj_list={}
        indeg=[0]*n
        for a,b in courses:
            lst=adj_list.get(a,[])
            lst.append(b)
            adj_list[a]=lst
            indeg[b]+=1
        q,ans=deque(),[]
        for i in range(n):
            if indeg[i]==0:
                q.append(i)
        while q:
            node=q.popleft()
            ans.append(node)
            for x in adj_list.get(node,[]):
                indeg[x]-=1
                if indeg[x]==0: 
                    q.append(x)
        return True if len(ans)==n else False
    def topo_dfs(courses,n):
        vis=[0]*n
        st=[]
        #make adj_list
        def rec(i):
            if vis[i]==2:return False
            vis[i]=1
            for x in adj_list.get(i,[]):
                if vis[x]==1:return True
                if vis[x]==2:continue
                temp=rec(x)
                if temp: return temp
            vis[i]=2
            st.append(i)
        for i in range(n):
            if vis[i]==0:
                temp=rec(i)
                if temp:return temp
        return st[::-1]
    def bipartite(edges,n):
        vis=[-1]*n
        # adj_list   
        def dfs(i,color):
            if vis[i]!=-1 and vis[i]!=color:return False
            if vis[i]==color: return True
            vis[i]=color
            for x in adj_list.get(i,[]):
                temp=dfs(x,1-color)
                if not temp:return temp
        for i in range(n):
            if vis[i]==-1:
                temp=dfs(i,0)
                if not temp:return temp
        return True
    def dijkstra(edges,n,s,d):
        #make adj_list but tuples(b,cost)
        dist=[float('inf')]*n
        heap=[]
        dist[s]=0
        heapq.heappush(heap,(0,s))
        while heap:
            dis,node=heapq.heappop(heap)
            if dis>dist[node]:continue
            for x in adj_list.get(node,[]):
                if dis+x[1]<dist[x[0]]:
                    heapq.heappush(heap,(dis+x[1],x[0]))
                    dist[x[0]]=dis+x[1]
        return dist[d] if dist[d]!=float('inf') else -1
    def bellman_ford(edges,n,s,d):
        dist=[float('inf')]*n
        dist[s]=0
        for _ in range(n-1):
            for a,b,wt in edges:
                dist[b]=min(dist[b],dist[a]+wt)
        for a,b,wt in edges:
            if dist[a]+wt<dist[b]: return True #cycle exists
        return dist[d] if dist[d]!=float('inf') else -1
    def floyd_warshall(edges,n):
        mat=[[float('inf')]*n for _ in range(n)]
        for a,b,wt in edges:
            mat[a][b]=wt
        for i in range(n):
            mat[i][i]=0
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    mat[i][j]=min(mat[i][j],mat[i][k]+mat[k][j])
        return mat
    def mst_kruskal(edges,n):
        def find(a,parent):
            if parent[a]==a:return a
            parent[a]=find(parent[a],parent)
            return parent[a]
        def union(a,b,parent):
            a_p=find(a,parent)
            b_p=find(b,parent)
            parent[a_p]=b_p
        def kruskal(edges):
            parent=[0]*n
            for i in range(n):
                parent[i]=i
            cost,count=0,0
            edges=sorted(edges,key=lambda x:x[2])
            for a,b,w in edges:
                a_p=find(a,parent)
                b_p=find(b,parent)
                if a_p==b_p:continue
                union(a_p,b_p,parent)
                count+=1
                cost+=w
                if count==n-1: return cost
        return kruskal(edges)
    def mst_prims(edges,n):
        #adj_list building from edges
        heap=[]
        heapq.heappush(heap,(0,0))
        # for a,b,w in edges:
        #     heapq.heappush(heap,(w,a,b))
        cost,count=0,0
        vis=[0]*n
        while heap:
            cst,b=heapq.heappop(heap)
            if vis[b]!=0:continue
            vis[b]=1
            count+=1
            cost+=cst
            if count==n-1:return cost
            for x in adj_list.get(b,[]):
                if vis[x[0]]==0:
                    heapq.heappush(heap,(x[1],x[0]))
        return -1
