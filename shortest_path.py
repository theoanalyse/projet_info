import parser as par
import graph as g
import dijkstra as d
import algorithm_A_star as aas
import algo_A_ETOILE as aAE

def create_port_graph():
    # setup the graph and its data 
    ports = par.parse_csv("input/coordinates.csv") 
    adjacency_matrix = par.parse_adjacency_matrix("input/adjacency_matrix.txt") 
    graph_ports = g.Graph() 
    
    # loop to add ports as node of the graph
    for port in ports:              
        graph_ports.add_vertex( port )

    # nested loop to add bonds between ports
    for i in range(len(adjacency_matrix)):
        for j in range(len(adjacency_matrix[i])):
            if adjacency_matrix[i][j] > 0:
                graph_ports.add_arc((ports[i], ports[j]), p=adjacency_matrix[i][j])

    return graph_ports, ports


graph_ports, ports = create_port_graph()
dict_path_dijkstra = d.dijkstra(graph_ports, ports[3])
dict_path_a_star = aAE.A_star(graph_ports, ports[1], ports[3])

# 3rd port is CNNGB and 1st port is FRFOS
d.display_shortest_path(dict_path_dijkstra, root_node=ports[1].get_name(), goal_node=ports[3].get_name())
d.display_shortest_path(dict_path_a_star, root_node=ports[1], goal_node=ports[3])
