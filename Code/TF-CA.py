import csv
from collections import defaultdict
from numpy import longdouble
import folium
import perlin_noise
import numpy as np
import heapq as hp
from IPython.display import display
def generacionGrafo():
    leer=False;
    dictStreetInd=defaultdict(int);
    dictPosInd=defaultdict(int);
    indexCalle=0;
    indexPos=0;
    graph=[[]];
    dic_interseccion={};
    dic_StreetNodetoPos={};
    with open('./Data/LecturaDatosStreetNy.csv') as f:
        reader= csv.reader(f);
        for row in reader:
            if not leer:
                leer=True;
                continue;
            positions=row[0].split(',');
            positions=[positions[0]]+[positions[-1]];
            for iposn in range(2):
                if not positions[iposn] in dictPosInd:
                    dictPosInd.update({positions[iposn]:indexPos});
                    dictPosInd.update({indexPos:positions[iposn]});
                    indexPos+=1;
                positions[iposn]=dictPosInd[positions[iposn]];
            
            for i in range(1,4):
                if not row[i] in dictStreetInd:
                    dictStreetInd.update({row[i]:indexCalle});
                    dictStreetInd.update({indexCalle:row[i]});
                    indexCalle+=1;
            
            node1,node2=positions;
            
            if (node1,node2) in dic_interseccion or (node1,node2) in dic_interseccion:
                continue;
            else:
                dic_StreetNodetoPos.update({(row[1],row[2]):node1});
                dic_StreetNodetoPos.update({(row[2],row[1]):node1});
                dic_StreetNodetoPos.update({(row[1],row[3]):node2});
                dic_StreetNodetoPos.update({(row[3],row[1]):node2});
                dic_interseccion.update({(node1,node2):1});
                dic_interseccion.update({(node2,node1):1});
            
            if node1>=len(graph):
                graph.append([]);
            graph[node1].append([node2,int(float(row[4])),None,None]);
            
            if node2>=len(graph):
                graph.append([]);
            graph[node2].append([node1,int(float(row[4])),None,None]);
    
    #print(graph);
    pushgraph_Text(graph,"./Results/grafoGeneratedText.txt");
    return graph,dictPosInd,dic_StreetNodetoPos;

    
def pushgraph_Text(graph:list(list()),s:str):
    with open(s,'w+',newline='\n') as f:
        for i in range(len(graph)):
            f.write(str(i)+": "+str(graph[i])+"\n");

def convertidorNodeToPos(dicPosId:dict(),node):
    pos=dicPosId.get(node);
    pos=pos.split(' ');
    pos=[(longdouble(pos[1])),(longdouble(pos[0]))];
    return pos;

def visualizeGraph(graph,dicPosId,m):
    n=len(graph);
    for node1 in range(n):
        for node2,dist,traf,newDist in graph[node1]:
            pos1=convertidorNodeToPos(dicPosId,node1);
            pos2=convertidorNodeToPos(dicPosId,node2);
            folium.CircleMarker(pos1,radius=5,color='red',fill=True,
            fill_color='#3186cc',fill_opacity=0.7,parse_html=False).add_to(m);
            folium.CircleMarker(pos2,radius=5,color='red',fill=True,
            fill_color='#3186cc',fill_opacity=0.7,parse_html=False).add_to(m);
            folium.ColorLine([pos1,pos2],colors=[50,51,52,56,55,54,53],colormap=['b','g','y','r'],nb_steps=4,weight=10,opacity=1).add_to(m);
    display(m);

def addTrafic(graph,dicPosId,traficoHora,hora,noise):
    n=len(graph);
    for node1 in range(n):
        for idNode2 in range(len(graph[node1])):
            node2,dist,traf,newDist=graph[node1][idNode2];
            pos1=dicPosId.get(node1);
            pos2=dicPosId.get(node2);
            pos1=pos1.split(' ');
            pos2=pos2.split(' ');
            x1=longdouble(pos1[1]);
            y1=longdouble(pos1[0]);
            x2=longdouble(pos2[1]);
            y2=longdouble(pos2[0]);

            traf=calcularTrafico(x1,y1,x2,y2,traficoHora,hora,noise)
            newDist=dist*traf;
            graph[node1][idNode2]=[node2,dist,traf,newDist];

def dikstra_recur(graph,start,end):
    n=len(graph);
    cost=[float('inf')]*n;
    visited=[False]*n;
    q=[];
    caminosCont=0;
    def dfs(at,path,c):
        nonlocal end;
        nonlocal caminosCont;
        path.append(at);
        visited[at]=True;
        if at==end:
            Paths.append(path);
            caminosCont+=1;
            if caminosCont==2:
                return Paths;
        for nei,peso,traf,newD in graph[at]:
            if visited[nei]: continue;
            f=newD+c;
            if f<cost[nei]:
                cost[nei]=f;
                hp.heappush(q,(f,nei,at));
        while q:
            w,at,prev=hp.heappop(q);
            dfs(at,path.copy(),w);
    
    Paths=[];
    return dfs(start,Paths,0);

def dijkstra(G, start,end):
    n = len(G)
    visited = [False]*n
    path = [-1]*n
    cost = [float('inf')]*n
    path[start]=-1;
    cost[start] = 0;
    pqueue = [(0, start,-1)];
    caminos=[];
    while pqueue:
        g, u,prev = hp.heappop(pqueue)
        if not visited[u]:
            if end==u:
                return path,cost;
            visited[u] = True;
        for v,w,tr,newd in G[u]:
            if not visited[v]:
                f = g + newd
                if f < cost[v]:
                    cost[v] = f
                    path[v] = u
                    hp.heappush(pqueue, (f, v, u))
    return path,cost;



def interfaz(graph, dicStreetNodesTOPos:dict(),PosInd:dict(),m):
    print("A donde quiere ir?");
    
    print("Intersecte dos calles como punto de partida\n");
    #node1Str1=input("1 calle: ");
    node1Str1="6 AVENUE";
    node1Str2="WEST   57 STREET";
    #node1Str2=input("2 calle: ");
    
    print("Intersecte dos calles como punto de parada\n");
    #node2Str1=input("1 calle: ");
    node2Str1="1 AVENUE";
    node2Str2="EAST   52 STREET";
    #node2Str2=input("2 calle: ");
    
    start=dicStreetNodesTOPos.get((node1Str1,node1Str2));
    end=dicStreetNodesTOPos.get((node2Str1,node2Str2));
    
    
    caminos,cost = dijkstra(graph, start,end);


    
def calcularTrafico(x1,y1,x2,y2,traficoHora,hora,noise):
    xm=(x1+x2)/2; ym=(y1+y2)/2;
    traf=abs(noise([xm,ym]));
    traf*=traficoHora[hora//2];
    return traf

def main():
    m = folium.Map(
        location=[ 40.72457376287186,-73.98749104757336 ],
        zoom_start=12,
        tiles='Stamen Terrain'
    )
    graph,dictPosInd,dictStretNodestoPos=generacionGrafo();
    #trafico:    12:00am - 2am -    4am-   6am-     8am   -10am
    traficoHora=[0.002, 0.001, 0.0002, 0.0010, 0.8233, 0.754   
                #12:00pm- 2pm-   4pm -   6pm -   8pm - 10pm
                ,0.706   ,0.855, 0.6005, 0.7544, 0.52, 0.34];
    noise = perlin_noise.PerlinNoise(octaves=10,seed=2);
    addTrafic(graph,dictPosInd,traficoHora,18,noise);
    interfaz(graph,dictStretNodestoPos,dictPosInd,m);
    #visualizeGraph(graph,dictPosInd,m);

if __name__=="__main__":
    main();
