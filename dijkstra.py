import graph as gr
import math as m
import coordinate as coord

#Adapter le code pour qu'il retourne le poids des arcs sommés
#Adapter le code pour qu'il donne juste les NOMS des ports, sinon on peut RIEN LIRE

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
    p_lisible = {}
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
                p[v] = u.get_name()
                p_lisible[v.get_name()] = (u.get_name(),d[v])
    return p_lisible

def display_shortest_path_dijkstra(dict_path, root_node, goal_node):
    path = [root_node]
    to_find = root_node
    while to_find != goal_node:
        for key in dict_path:
            if key == to_find:            
                name, time_to_travel = dict_path[key]
                path.append(name)
                to_find = name
    path.reverse()
    print('best path = ', path, "time = ", dict_path[root_node])
            