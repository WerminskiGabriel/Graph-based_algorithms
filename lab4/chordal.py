import copy
import os
import dimacs


def checkLexBFS( G , vs ) :
    n = len( G )
    pi = [None] * n
    for i , v in enumerate( vs ) :
        pi[v] = i

    for i in range( n - 1 ) :
        for j in range( i + 1 , n - 1 ) :
            Ni = G[vs[i]]
            Nj = G[vs[j]]

            verts = [pi[v] for v in Nj - Ni if pi[v] < i]
            if verts :
                viable = [pi[v] for v in Ni - Nj]
                if not viable or min( verts ) <= min( viable ) :
                    return False
    return True


def checkPEO( G , vs ) :
    n = len( vs )
    position = { }

    for i , v in enumerate( vs ) :
        position[v] = i

    for i , v in enumerate( vs ) :
        RN_v = { u for u in G[v] if position[u] < i }

        if not RN_v :
            continue

        parent_v = max( RN_v , key = lambda u : position[u] )

        RN_parent = { u for u in G[parent_v] if position[u] < position[parent_v] }

        if not (RN_v - { parent_v }) <= RN_parent :
            return False

    return True


def chordal( G ) :
    def initializeNodes( ) :
        Nodes = []
        remainingNodes = set( )
        for u in range( len( A ) ) :
            Nodes.append( set( ) )
            remainingNodes.add( u )
            for v , _ in A[u] :
                Nodes[u].add( v )
        return Nodes , remainingNodes

    A , V = G.A , G.V
    Nodes , remainingNodes = initializeNodes( )
    Result = []

    L = [remainingNodes.copy( )]  # Collection of sets

    while L :
        while L and len( L[-1] ) == 0 :  # remove empty sets
            L.pop( )

        if not L :
            break

        v = L[-1].pop( )
        Result.append( v )

        new_L = []

        for X in L :
            Y = set( )  # neighbours of v in Y
            K = set( )  # else in K

            for u in X :
                if u in Nodes[v] :
                    Y.add( u )
                else :
                    K.add( u )

            if K :
                new_L.append( K )
            if Y :
                new_L.append( Y )

        L = new_L

    return checkPEO( Nodes , Result )


dimacs.Tests( os.path.abspath( "chordal" ) ,
              chordal ,
              "loadWeightedGraph" ,
              True ,
              { "clique200" , "grid100x100" }
              )
