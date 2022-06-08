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


def pushgraph_Text(graph:list(list()),s:str):
    with open(s,'w+',newline='\n') as f:
        for i in range(len(graph)):
            f.write(str(i)+": "+str(graph[i])+"\n");

def main():
    graph=generacionGrafo();
    print(graph);

if __name__=="__main__":
    main();

