import csv
from collections import defaultdict
from numpy import array, longdouble
import folium
import opensimplex
def generacionGrafo():
    leer=False;
    dictStreetInd=defaultdict(int);
    dictPosInd=defaultdict(int);
    indexCalle=0;
    indexPos=0;
    graph=[[]];
    dic_interseccion={};
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
                dic_interseccion.update({(node1,node2):1});
                dic_interseccion.update({(node2,node1):1});
            
            if node1>=len(graph):
                graph.append([]);
            graph[node1].append([node2,int(float(row[4])),None,None]);
            
            if node2>=len(graph):
                graph.append([]);
            graph[node2].append([node1,int(float(row[4])),None,None]);
    
    print(graph);
    pushgraph_Text(graph,"./Results/grafoGeneratedText.txt");
    return graph;

def pruebaCalleHora():
    #punto medio de la calle;
    x1=345455; y1=512725;
    x2=85817; y2=82642;
    xm=(x1+x2)/2;
    ym=(y1+y2)/2;
    hora=18;
    info1=opensimplex.noise3(xm,ym,hora);
    info2=opensimplex.noise3(xm+0.0003,ym+0.0008,hora);
    #dos calles cercanas a la misma hora deberia de ser maso igual
    print(info1);
    print(info2);
    #una calle a una hora cercana deberia de ser maso igual
    info1=opensimplex.noise3(xm,ym,hora);
    info2=opensimplex.noise3(xm,ym,hora+0.002);
    print(info1);
    print(info2);
    #los resultados son correctos.
    #-0.16251390572196256
    #-0.16168611734998933
    
    #-0.16251390572196256
    #-0.1647895170897928
    
def pushgraph_Text(graph:list(list()),s:str):
    with open(s,'w+',newline='\n') as f:
        for i in range(len(graph)):
            f.write(str(i)+": "+str(graph[i])+"\n");

def main():
    graph=generacionGrafo();
    print(graph);

if __name__=="__main__":
    #main();
    pruebaCalleHora();

