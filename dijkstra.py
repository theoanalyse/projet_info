import graph as gr
import math as m

def find_min(queue, d):
    min = m.inf
    vertex_min = None
    for vertex in queue.keys():
        if d[vertex] <= min:
            min = d[vertex]
            vertex_min = vertex
    return vertex_min


def dijkstra(G, root_vertex):
    d = {}
    p = {}
    queue = G.vertices.copy()
    for vertex in queue:
        d[vertex] = m.inf
        p[vertex] = None
    d[root_vertex] = 0
    while queue != {}:
        u = find_min(queue, d)
        queue.pop(u)
        for v in G.outgoing_neighbours(u):
            if d[v] > d[u] + G.arc_weight((u, v)):
                d[v] = d[u] + G.arc_weight((u, v))
                p[v] = u
    return d,p


def create_graph_example():
    g = gr.Graph()
    g.add_vertex("A")
    g.add_vertex("B")
    g.add_vertex("C")
    g.add_vertex("D")
    g.add_vertex("E")
    g.add_vertex("F")
    g.add_vertex("G")
    g.add_arc(("A", "B"), 3)
    g.add_arc(("A", "E"), 10)
    g.add_arc(("B", "C"), 6)
    g.add_arc(("B", "D"), 13)
    g.add_arc(("C", "D"), 6)
    g.add_arc(("E", "D"), 9)
    g.add_arc(("E", "F"), 1)
    g.add_arc(("F", "D"), 3)
    g.add_arc(("C", "G"), 15)
    g.add_arc(("D", "G"), 3)
    return g

if __name__ == "__main__":
    g = create_graph_example()
    print(dijkstra(g, "A"))
