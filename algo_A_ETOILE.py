import graph as gr
import coordinate as coord


def heuristic(vertex1, vextex2) :
    return vertex1.distance(vertex2)


def find_min(queue, dict):
    min = m.inf
    vertex_min = None
    for vertex in queue:
        if dict[vertex] <= min:
            min = d[vertex]
            vertex_min = vertex
    return vertex_min

def A_star(Graph, start, finish) :
    g_score = {}
    f_score = {}
    closed_list = []
    queue = [start]
    path = {}
    g_score[start] = 0
    f_score[start] = g_score[start] + heuristic(start, finish)
    while F != [] :
        u = find_minimum(queue, f_score)
        queue.pop(u)
        if u == finish :
            return (p, g_score[finish])
        closed_list+= [u]

        for v in Graph.outgoing_neighbors() :
            if not(v in closed_list) :
                g_score_try = g_score[u] + Graph.arc_weight((u,v))
                if not(v in queue) or g_score_try < g_score[v] :
                    path[v] = u
                    g_score[v] = g_score_try
                    f_score[v] = g_score[v] + heuristic(v, finish)
                    if not (v in queue) :
                        queue += [v]
    return "a critical error has occured"