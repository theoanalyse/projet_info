import math as m
import parser as par
import graph as g
import dijkstra as d

ports = par.parse_csv("input/coordinates.csv")
adjacency_matrix = par.parse_adjacency_matrix("input/adjacency_matrix.txt")

graph_ports = g.Graph()
for port in ports:
    x, y, port_name = port.get_coordinates_radians()
    graph_ports.add_vertex( (port_name, x, y) )

# print(graph_ports.list_vertices())

available_ports = 0
for i in range(len(adjacency_matrix)):
    for j in range(len(adjacency_matrix[i])):
        if adjacency_matrix[i][j] != -1:
            available_ports += 1
print(available_ports)
print(graph_ports.is_connex())