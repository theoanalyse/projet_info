import graph as gr
import coordinate as coord


def heuristic(vertex1, vextex2) :
    return vertex1.distance(vertex2)

def extract_minimum(F) :
    return

def A_star(Graph, start, finish) :
    g_score = {}
    f_score = {}
    closed_list = []
    F = [start]
    p = {}
    g_score[start] = 0
    f_score[start] = g_score[start] + heuristic(start, finish)

    while F != [] :
        u = extract_minimum(F)
        if u == finish :
            return (p, g_score[finish])
        closed_list+= [u]

        for v in Graph.outgoing_neighbors() :
            if not(v in closed_list) :
                g_score_try = g_score[u] + g