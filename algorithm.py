import json
import random as r
import math
import heapq as hq
import TFComple as tf;



def transformGraph():
    dictPosId={};
    dic_StreetNodetoPos={};
    G,dictPosId=tf.generateGraph();
    Loc=tf.getLoc(G,dictPosId);
    return G, Loc,dictPosId
    # n, m = 90, 40
    # Loc = [(i * 100 - r.randint(145, 155), j * 100 - r.randint(145, 155))
    # for i in range(1, n + 1) for j in range(1, m + 1)]
    # G = [[] for _ in range(n * m)]
    # for i in range(n):
    #     for j in range(m):
    #         adjs = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
    #         r.shuffle(adjs)
    #         for u, v in adjs:
    #             if u >= 0 and u < n and v >= 0 and v < m:
    #                 G[i * m + j].append((u * m + v, r.randint(1, 345353)))
    # return G, Loc

def bfs(G, s):
    n = len(G)
    visited = [False]*n
    path = [-1]*n # parent
    queue = [(s,0)]
    visited[s] = True
    cost=[math.inf]*n;
    while queue:
        u,g = queue.pop(0)
        for v, _,_,w in G[u]:
            if not visited[v]:
                f=w+g;
                cost[v]=min(f,cost[v])
                visited[v] = True
                path[v] = u
                queue.append((v,f));

    return path,cost

def dfs(G, s):
    n = len(G)
    path = [-1]*n
    visited = [False]*n
    stack=[s];
    while stack:
        u=stack.pop();
        visited[u] = True
        r.shuffle(G[u]);
        for v,_,_,w in G[u]:
            if not visited[v]:
                path[v] = u
                stack.append(v);
    
    return path


def dijkstra(G, s):
    n= len(G)
    visited= [False]*n
    path= [-1]*n
    cost= [math.inf]*n

    cost[s]= 0
    pqueue= [(0, s)]
    while pqueue:
        g, u= hq.heappop(pqueue)
        if not visited[u]:
            visited[u]= True
            for v, _,_,w in G[u]:
                if not visited[v]:
                    f= g + w
                    if f < cost[v]:
                        cost[v]= f
                        path[v]= u
                        hq.heappush(pqueue, (f, v))

    return path, cost

def reconstruccionCost(prev,cost,s,t):
    at=t;
    costTOTAL=0;
    while at!=-1:
        costTOTAL+=cost[at];
        at=prev[at];

G, Loc,dictPosId = transformGraph()
# G, Loc = transformGraph()
addtrafico=[False];
def graph():
    return json.dumps({"loc": Loc, "g": G})

def paths(s, t):
    if not addtrafico[0]:
        tf.addTrafic(G,dictPosId); 
        addtrafico[0]=True;
    bestpath, cost = dijkstra(G, s)
    path2,cost1=tf.caminoAlternativo(G,s,t)
    path1,cost2=bfs(G,s);
    print('Distancia Dijkstra: ',cost[t]);
    print('Distancia Propio: ',cost1[t]);
    print('Distancia BFS: ',cost2[t]);
    #path2=dfs(G,s);
    #path1,path2=bfs(G,s),dfs(G,s);

    return json.dumps({"bestpath": bestpath, "path1": path1, "path2": path2})