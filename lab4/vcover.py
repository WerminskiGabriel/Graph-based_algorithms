import os
import dimacs
from lexbfs import lexBFS


def vcover( G ) :
    Nodes = []
    for u in range( len( G.A ) ) :
        Nodes.append( set( ) )
        for v , _ in G.A[u] :
            Nodes[u].add( v )

    order = lexBFS( Nodes )

    reverse_order = list( reversed( order ) )

    I = set( )

    for v in reverse_order :
        N = Nodes[v]

        if I.isdisjoint( N ) :
            I.add( v )

    n = len( Nodes )
    return n - len( I )


dimacs.Tests(
    os.path.abspath( "vcover" ) ,
    vcover ,
    "loadWeightedGraph" ,
    True ,
    set( )
)
