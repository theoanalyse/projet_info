import graph as gr
import coordinate as coord
import math as m

'''
#To be removed
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distance(self, other):
        return m.sqrt( (self.x - other.x)**2 + (self.y - other.y)**2)
'''


def heuristic(vertex1, vertex2) :
    return vertex1.distance(vertex2)


def is_empty(l):
    return len(l) == 0


def extract_minimum(queue, dico) :
    min = m.inf
    vertex_min = None
    for vertex in queue:
        print(dico, "v = ", vertex)
        if dico[vertex] <= min:
            min = dico[vertex]
            vertex_min = vertex
    return vertex_min


def A_star(graph, start, end) :
    g_score = {}
    f_score = {}
    path = {}
    queue = [start]
    closed_list = []
    g_score[start] = 0
    f_score[start] = g_score[start] + heuristic(start, end)

    while not ( is_empty(queue) ):
        u = extract_minimum(queue, f_score)
        queue.remove(u)
        if u is None:
            return('erreur, pas de min trouvé')
        print("u", u.get_name())
        if u == end:
            return path, g_score[end]
        closed_list.append(u)
        for v in graph.outgoing_neighbours(u):
            if not ( v in closed_list ):
                possible_g_score = g_score[u] + graph.arc_weight( (u, v) )
                if ( not (v in queue) or possible_g_score < g_score[v]):
                    path[v] = u
                    g_score[v] = possible_g_score
                    f_score[v] = g_score[v] + heuristic(v, end)
                    if not (v in queue):
                        queue.append(v)


if __name__ == "__main__":
    P1 = coord.Coordinate(10, 10, "P1")
    P2 = coord.Coordinate(12, 12, "P2")
    P3 = coord.Coordinate(3 , 4 , "P3")
    P4 = coord.Coordinate(5 , 9 , "P4")

    graph = gr.Graph()
    graph.add_vertex(P1)
    graph.add_vertex(P2)
    graph.add_vertex(P3)
    graph.add_vertex(P4)
    graph.add_arc((P1, P2))
    graph.add_arc((P1, P3))
    graph.add_arc((P2, P3))
    graph.add_arc((P3, P4))

    dico = A_star(graph, P1, P4)
    print(dico)