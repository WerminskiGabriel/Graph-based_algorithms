import dimacs
import os
from queue import PriorityQueue

def Stoer_Wagner( G ) :
    def initializeNodes() :
        for u in range( len( A ) ) :
            Nodes[u] = Node( )
            for v , w in A[u] :
                Nodes[u].addEdge( v , w )
    class Node :
        def __init__( self ) :
            self.edges = { }  # słownik  mapujący wierzchołki do których są krawędzie na ich wagi
            self.merged = set()

        def addEdge( self , to , weight ) :
            self.edges[to] = self.edges.get( to , 0 ) + weight # dict.get( key , deafult If dict[key] does not exit )

        def delEdge( self , to ) :
            del self.edges[to]

    def mergeVertices( x , y ) :
        edgesX = Nodes[x].edges
        edgesY = Nodes[y].edges

        for neighbor , weight in edgesY.items() : # dodajemy z y do x
            if neighbor == x :
                continue
            if neighbor in edgesX :
                edgesX[neighbor] += weight
            else :
                Nodes[x].addEdge( neighbor , weight )

        for neighbor, weight in Nodes[y].edges.items( ) : # nadpisujemy wszystko co idzie do y
            if neighbor == x :
                continue
            Nodes[neighbor].delEdge( y )
            Nodes[neighbor].addEdge( x , weight )
        del Nodes[y]
        if y in edgesX :
            del edgesX[y] # usun wskaznik z x na y

    def minimumCutPhase( ) :
        A = set( )
        remaining = set( Nodes.keys( ) )

        first = list( Nodes.keys() )[0]

        A.add( first )
        remaining.remove( first )
        s , t = first , first

        while remaining :
            max_weight = -1
            best_v = None
            for v in remaining :
                weight_to_A = sum( Nodes[v].edges.get( u , 0 ) for u in A )
                if weight_to_A > max_weight :
                    max_weight = weight_to_A
                    best_v = v
            s = t # przesuwamy
            t = best_v
            A.add( best_v )
            remaining.remove( best_v )

        cut_value = sum( Nodes[t].edges.values( ) )
        mergeVertices( s , t )
        return cut_value

    min_cut = float( "inf" )
    A , V = G.A , G.V
    Nodes = {}

    initializeNodes()
    while len( Nodes ) > 1 :
        cut = minimumCutPhase()
        min_cut = min( min_cut , cut )
    return min_cut

"""
G = dimacs.Graph( "Graphs" , 'simple' )
G.loadWeightedGraph( )
print( Stoer_Wagner( G ) , G.S )
"""

dimacs.Tests( os.path.abspath("Graphs") , Stoer_Wagner , "loadWeightedGraph" , True , { "clique200" , "grid100x100" } )

