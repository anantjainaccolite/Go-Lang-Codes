def depth (root,edges,d,visited):
    w=d
    visited[root-1]=True
    for i in edges.keys():
        for j in edges[i] :
            if(visited[j-1]==False):
                d=max(d,depth(j,edges,w+1,visited))                
    return d
   
def delete(edges):
    for i in edges.values() :
        for j in to_delete:
            if(j in i ):
                i.remove(j)
        
def process(root,edges,visited,w):
    visited[root-1]=True
    flag=False
    for i in edges[root]:
        if(visited[i-1]==False):
            flag= process(i,edges,visited,w) or flag       
    if(flag==False and w[root-1]%2==0):
        del(edges[root])
        to_delete.append(root)
        return False
    return True
  
t=int(input())
while(t):
    N=int(input())
    edges={}
    to_delete=[]
    for _ in range (N-1):
            x,y=map(int,input().split())
            if(edges.get(x)):
                edges[x].append(y)
            else:
                edges[x]=[y]
            if(edges.get(y)):
                edges[y].append(x)
            else:
                edges[y]=[x]
    w=list(map(int,input().split()))
    print("Depth :  ",depth(1,edges,0,visited))
    visited=[False]*N
    process(1,edges,visited,w)
    delete(edges)
    visited=[False]*N
    print("Nodes in Tree: ", len(edges))
    print("Depth of Tree: ",depth(1,edges,0,visited))
    t-=1
