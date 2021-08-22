class Graph:
    def __init__(self,nodes):
        self.nodes = nodes
        self.edges = {}
        for i in self.nodes:
            self.edges[i] = []

    def add_edge(self, pair):
        start,end = pair
        if start not in self.edges.keys():
            self.edges[start] = []       
            self.edges[start].append(end)
            return 1
        elif end in self.edges[start]:
            self.edges[start].append(end)
            return -1

    def children(self,node):
        return self.edges[node]
    def nodes(self):
        return str(self.nodes)
    def __str__(self):
        return str(self.edges)

    def add_node(self,n):
        if n not in self.nodes:
            self.nodes.append(n)
            return 1
        else:
            return -1

    def del_node(self,n):
        if n not in self.nodes:
            return -1
        elif n in self.nodes:
            self.nodes.remove(n)
            return 1

    def del_edge(self,pair):
        start,end = pair
        if start not in self.nodes:
            return -1
        elif end not in self.edges[start]:
            self.edges[start].remove(end)
            return 1

def bfsfull(g,node):
    q = [node]
    r = []
    visited = set()
    while q:
        vertex = q.pop(0)
        if vertex not in visited:
            visited.append(vertex)
            print(vertex)
            q.extend(g.edges[vertex])
        if len(q)==0 and len(visited) != len(g.nodes):
            for e in g.nodes:
                for e not in visited:
                    r.append(e)
            q.append(choice(r))
return visited


    
g = Graph([1,2,3,4,5,6,7,8])
elst = [(1,2),(1,3),(2,8),(3,5),(3,4),(5,6),(6,4),(6,7)]
for i in elst:
    g.add_edge(i)
print(g.edges)
bfsfull(g,5)
