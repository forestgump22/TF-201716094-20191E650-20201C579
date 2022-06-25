import json
import TFComple
from collections import defaultdict
G=[[]];
def graph():
    G,dictPosId,dictStretNodestoPos=list(list()),defaultdict(),defaultdict();
    G = TFComple.generacionGrafo(G,dictPosId,dictStretNodestoPos);
    Loc = TFComple.getLoc(G,dictPosId);
    response = {"loc": Loc, "g": G}

    return json.dumps(response)

def paths():
    start=0; end=0;
    
    bestpath,path1,path2=\
    TFComple.getBestP2Alter(G,start,end);

    response = {"bestpath": bestpath, "path1": path1, "path2": path2}

    return json.dumps(response)

