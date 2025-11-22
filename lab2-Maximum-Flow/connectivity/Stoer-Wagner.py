import dimacs
import os
from collections import deque

def StoerWagner( G ) :

    def edmondKarps(  s , t ) :

        residualGraph = [[0 for _ in range( V )] for _ in range( V )]
        for u in range( V ) :
            for v , w in A[u] :
                residualGraph[u][v] = 1
                residualGraph[v][u] = 1

        q = deque( )
        q.append( s )

        inf = float( "inf" )

        parent = [-1] * V
        minFlow = [inf] * V

        maxFlow = 0

        while q :
            u = q.popleft( )
            if u == t :
                currentFlow = minFlow[u]
                while u != s :
                    p = parent[u]
                    residualGraph[p][u] -= currentFlow
                    residualGraph[u][p] += currentFlow
                    u = p
                maxFlow += currentFlow
                parent = [-1] * V
                minFlow = [inf] * V
                q = deque( )
                q.append( s )
                continue

            for v in range( V ) :

                if parent[v] == -1 and residualGraph[u][v] > 0 :
                    parent[v] = u
                    minFlow[v] = min( residualGraph[u][v] , minFlow[u] )

                    q.append( v )

        return maxFlow

    V = G.V
    A = G.A

    s = 0
    result = float( 'inf' )

    for t in range( 1 , V ) :
        result = min( result , edmondKarps( s , t ) )

    return result

dimacs.Tests(os.path.abspath("Graphs"), StoerWagner, "loadDirectedWeightedGraph", True  , { "clique200" , "grid100x100" } )
