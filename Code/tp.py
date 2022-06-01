import csv
from collections import defaultdict

from numpy import array
 
def cambiando_datos():
    leer=False;
    dictStreetInd=defaultdict(int);
    dictPosInd=defaultdict(int);
    indexCalle=0;
    indexPos=0;
    newFile=open('FileNew.csv','w+',newline='');
    with open('LecturaDatosStreetNy.csv') as f:
        reader= csv.reader(f);
        write=csv.writer(newFile);
        for row in reader:
            if not leer:
                leer=True;
                continue;
            positions=row[0].split(',');
            positions=[positions[0]]+[positions[-1]];
            for iposn in range(2):
                if not positions[iposn] in dictPosInd:
                    dictPosInd.update({positions[iposn]:indexPos});
                    indexPos+=1;
                positions[iposn]=dictPosInd[positions[iposn]];#cambiamos valor  a positions solo es como un formateo
            row[0]=positions;
            for i in range(1,4):
                if not row[i] in dictStreetInd:
                    dictStreetInd.update({row[i]:indexCalle});
                    indexCalle+=1;
                row[i]=dictStreetInd[row[i]];
            write.writerow(row);
    newFile.close();
    
    printallinfo_streetsNY(dictStreetInd,'streetsIDFile.txt');

def printallinfo_streetsNY(dic:dict,s):
    filestreets=open(s,'w+',newline='\n');

    for key in dic.keys():
        filestreets.write(str(key)+":"+str(dic.get(key))+"\n");
    filestreets.close();

def generargrafo():
    i=0;
    graph=[[]];
    dic_nodos={};
    leer=False;
    dic_interseccion={};
    with open('FileNew.csv') as f:
        reader=csv.reader(f);
        for row in reader:
            if not leer:
                leer=True;
                continue;
            
            nodes=row[0];
            nodes=nodes.split(',');
            node1=int(nodes[0].removeprefix("["));
            node2=int(nodes[-1].removesuffix("]"));
            nodes=[node1]+[node2];
            
            for i in range(2):
                dic_nodos.update({nodes[i]:(row[1],row[i+2])});
            
            node1,node2=nodes;
            
            if (node1,node2) in dic_interseccion or (node1,node2) in dic_interseccion:
                continue;
            else:
                dic_interseccion.update({(node1,node2):1});
                dic_interseccion.update({(node2,node1):1});
            if node1<len(graph):
                graph[node1].append([node2,int(float(row[4]))]);
            else:
                graph.append([node2,int(float(row[4]))]);
            
            if node2<len(graph):
                graph[node2].append([node1,int(float(row[4]))]);
            else:
                graph.append([node1,int(float(row[4]))]);
    
    print(graph);
    pushgraph_Text(graph,"grafoGeneratedText.txt");

def pushgraph_Text(graph:list(list()),s:str):
    
    with open(s,'w+',newline='\n') as f:
        for i in range(len(graph)):
            f.write(str(i)+": "+str(graph[i])+"\n");


if __name__=="__main__":
    cambiando_datos();
    generargrafo();

