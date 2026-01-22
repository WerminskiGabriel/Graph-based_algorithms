import os
import dimacs
from lexbfs import lexBFS


def coloring( G ) :
    Nodes = []
    for u in range( len( G.A ) ) :
        Nodes.append( set( ) )
        for v , _ in G.A[u] :
            Nodes[u].add( v )

    order = lexBFS( Nodes )

    # greedy coloring in lexbfs order
    color = { }

    for v in order :
        used_colors = set( )
        for u in Nodes[v] :
            if u in color :
                used_colors.add( color[u] )

        # we find smallest color that has not been used
        c = 1
        while c in used_colors :
            c += 1

        color[v] = c

    return max( color.values( ) ) if color else 0


dimacs.Tests(
    os.path.abspath( "coloring" ) ,
    coloring ,
    "loadWeightedGraph" ,
    True ,
    { }
)
