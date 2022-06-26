from cmath import atan
import json
from flask import Flask
import TFComple as TFComple

G=[[]];
dictStretNodestoPos={};
dictPosId={};
def graph():
    TFComple.generacionGrafo(G,dictPosId,dictStretNodestoPos);
    Loc = TFComple.getLoc(G,dictPosId);
    
    response = {"loc": Loc, "g": G}

    return json.dumps(response)

def paths():
    TFComple.addTrafic(G,dictPosId);
    start=0; end=0;
    print("A donde quiere ir?\n");
    print("Intersecte dos calles como punto de partida\n");
    #node1Str1=input("1 calle: ");
    node1Str1="6 AVENUE";
    print(node1Str1);
    node1Str2="WEST   57 STREET";
    #node1Str2=input("2 calle: ");
    print("Intersecte dos calles como punto de parada\n");
    #node2Str1=input("1 calle: ");
    node2Str1="1 AVENUE";
    node2Str2="EAST   52 STREET";
    #node2Str2=input("2 calle: ");
    
    start=dictStretNodestoPos.get((node1Str1,node1Str2));
    end=dictStretNodestoPos.get((node2Str1,node2Str2));
    
    bestpath,path1 =TFComple.getBestP2Alter(G,start,end);
    bestpath=[10,23,50];
    response = {"bestpath": bestpath, "path1": path1}

    return json.dumps(response)

# graph();
# paths();