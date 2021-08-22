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


import numpy as np
a = np.zeros ((4,4),dtype = int)
a[0][1] = 1
a[1][2] = 1
a[2][3] = 1
print(a)
a = np.dot (a,a) + a
print(a)
a = np.dot (a,a) + a
print(a)

for i in range(0,4):
    for j in range(0,4):
        if not i == j:
            print("{0} reaches {1}: {2}".format(i+1,j+1,bool(a[i][j])))
