class Graph:
    def __init__(self):
        self.vertices = {}
        self.arcs = {}

    def add_vertex(self, v):
        if v in self.vertices.keys():
            pass
        else:
            self.vertices[v] = {}

    def add_arc(self, a, p=1):
        #the arc is a tuple(v1, v2) joining two vertex
        v1, v2 = a
        self.add_vertex(v1)
        self.add_vertex(v2)
        if a in self.arcs.keys() and self.arcs[a] == p:
            pass
        else:
            self.arcs[a] = p
            self.vertices[v1][v2] = p

    def remove_arc(self, a):
        if a in self.arcs.keys():
            self.arcs.pop(a)
        else:
            pass

    def remove_vertex(self, v):
        tmp_arcs = self.arcs.copy()
        if v in self.vertices.keys():
            self.vertices.pop(v)
            for arc in tmp_arcs:
                v1, v2 = arc
                if (v1 == v) or (v2 == v):
                    self.arcs.pop(arc)
        else:
            pass

    def list_vertices(self):
        vert = []
        for vertex in self.vertices.keys():
            vert.append(vertex)
        return vert

    def outgoing_neighbours(self, v):
        return list(self.vertices[v].keys())

    def ingoing_neighbours(self, s):
        ingoing = []
        for arc in self.arcs.keys():
            v1, v2 = arc
            if s == v2:
                ingoing.append(v1)
        return ingoing

    def arc_weight(self, arc):
        return self.arcs[arc]

    def is_connex(self) :
        for v in self.vertices :
            if self.ingoing_neighbours(v) == [] and self.   (v) == [] :
                return (False, v)
        return True

    #Check whether or not the graph is supposed to be oriented - and how do we treat unoriented graphs ?
    
    def density(self) :
        return (len(self.arcs)/(len(self.vertices))*(len(self.vertices)-1))


'''
if __name__ == "__main__":
    g = Graph()
    g.add_vertex(0)
    g.add_vertex(1)
    g.add_vertex(2)
    arc_AB = (0, 1)
    arc_CA = (2, 0)
    arc_DA = (3, 0)
    g.add_arc(arc_AB, 3)
    print(g.vertices)
    print (g.is_connex())
    print(g.density())
''' 