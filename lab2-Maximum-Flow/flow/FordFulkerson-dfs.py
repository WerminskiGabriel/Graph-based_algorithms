import dimacs
import os

def FordFulkerson( G ) :


    def dfs( u , parent , flowCapacity) :
        if u == t :
            return flowCapacity

        for v in range( V ) :

            if parent[v] == -1 and residualGraph[u][v] > 0 :
                parent[v] = u

                newFlow = dfs( v , parent , min( flowCapacity , residualGraph[u][v] ) )

                if newFlow > 0 :
                    return newFlow
                parent[v] = -1
        return 0

    A = G.A
    V = G.V

    s = 0
    t = V-1

    inf = float( "inf" )

    residualGraph = [ [ 0 for _ in range( V ) ] for _ in range( V ) ]
    for u in range( V ) :
        for v,w in A[u] :
            residualGraph[u][v] = w

    maxFlow = 0

    while True :

        parent = [-1] * V
        currentFlow = dfs( s , parent , inf )

        if currentFlow == 0 :
            break

        maxFlow += currentFlow

        v = t
        while v != s :
            u = parent[v]

            residualGraph[u][v] -= currentFlow

            residualGraph[v][u] += currentFlow

            v = u

    return maxFlow


G = dimacs.Graph( "Graphs" , 'simple' )
G.loadDirectedWeightedGraph()
print( FordFulkerson( G ) , G.S )

dimacs.Tests( os.path.abspath("Graphs")  , FordFulkerson, "loadDirectedWeightedGraph" , False )
