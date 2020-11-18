import math as m
import parser as par
import graph as g
import dijkstra as d

ports = par.parse_csv("input/coordinates.csv")
adjacency_matrix = par.parse_adjacency_matrix("input/adjacency_matrix.txt")

graph_ports = g.Graph()

for port in ports:
    graph_ports.add_vertex( port )


# print(graph_ports.list_vertices())



for i in range(len(adjacency_matrix)):
    for j in range(len(adjacency_matrix[i])):
        if adjacency_matrix[i][j] > 0:
            graph_ports.add_arc((ports[i], ports[j]), p=adjacency_matrix[i][j])
            

print(d.dijkstra(graph_ports, ports[3]))

#"hello !"

