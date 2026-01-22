def lexBFS( Nodes , start = None ) :
    n = len( Nodes )

    remainingNodes = set( range( n ) )

    if start is None :
        L = [remainingNodes.copy( )]
    else :
        all_vertices = remainingNodes.copy( )
        all_vertices.remove( start )
        L = [all_vertices , { start }]

    Result = []

    while L :
        while L and len( L[-1] ) == 0 :
            L.pop( )

        if not L :
            break

        v = L[-1].pop( )
        Result.append( v )

        new_L = []

        for X in L :
            Y = set( )  # sąsiedzi v w X
            K = set( )  # reszta X

            for u in X :
                if u in Nodes[v] :
                    Y.add( u )
                else :
                    K.add( u )

            # Dodaj K, potem Y (kolejność ważna!)
            if K :
                new_L.append( K )
            if Y :
                new_L.append( Y )

        L = new_L

    return Result


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
