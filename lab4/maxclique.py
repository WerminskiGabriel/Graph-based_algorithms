import os
import dimacs
from lexbfs import lexBFS


def maxclique( G ) :
    Nodes = []
    for u in range( len( G.A ) ) :
        Nodes.append( set( ) )
        for v , _ in G.A[u] :
            Nodes[u].add( v )

    order = lexBFS( Nodes )

    n = len( order )
    position = { }

    for i , v in enumerate( order ) :
        position[v] = i

    max_clique = 0

    for i , v in enumerate( order ) :
        RN_v = set( )
        for u in Nodes[v] :
            if position[u] < i :
                RN_v.add( u )

        clique_size = len( RN_v ) + 1

        if clique_size > max_clique :
            max_clique = clique_size

    return max_clique


dimacs.Tests(
    os.path.abspath( "maxclique" ) ,
    maxclique ,
    "loadWeightedGraph" ,
    True ,
    { "clique200" , "grid100x100" }
)
