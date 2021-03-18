import  queue
import numpy
import os
import time

f1 = "C:/Users/Centaure Emeline/PycharmProjects/TME1_CPA/RESSOURCES/graphes/com-amazon.ungraph.txt"
f2 = "C:/Users/Centaure Emeline/PycharmProjects/TME1_CPA/RESSOURCES/graphes/com-lj.ungraph.txt"
f3 = "C:/Users/Centaure Emeline/PycharmProjects/TME1_CPA/RESSOURCES/graphes/com-orkut.ungraph.txt"
#f4 = "C:/Users/Centaure Emeline/PycharmProjects/TME1_CPA/RESSOURCES/graphes/com-amazon.ungraph.txt"

liste_graphes = [f1, f2, f3]

#EX1 nb of edges and nodes
#test
def get_nb_nodes(f) :
    file_to_read = open(f, "r")
    nb_line = 0
    nb_nodes = 0
    set_nodes = set()
    for line in file_to_read:
        if nb_line >= 4:
            p = line.split()
            if p[0] not in set_nodes:
                set_nodes.add(p[0])
                nb_nodes = nb_nodes + 1
            if p[1] not in set_nodes:
                set_nodes.add(p[1])
                nb_nodes = nb_nodes + 1
        nb_line = nb_line + 1
    file_to_read.close()
    return nb_nodes

def get_nb_edges(f) :
    file = open(f, "r")
    file.seek(0)

    nb_line = 0
    nb_edges = 0
    set_edges = set()
    for line in file:
        if nb_line >= 4:
            p = line.split()
            if frozenset([p[0],p[1]]) not in set_edges:
                set_edges.add(frozenset([p[0],p[1]]))
                nb_edges = nb_edges + 1
        nb_line = nb_line + 1
    file.close()
    return nb_edges

def list_of_edges(f):
    file= open(f, "r")
    list_edges = []
    nb_line = 0

    for line in file:
        if nb_line >= 4:
            pairofnode = line.split()
            list_edges.append((pairofnode[0],pairofnode[1]))
        nb_line = nb_line + 1
    return list_edges

def adjacency_matrix(f):
    file = open(f)
    amatrix = []
    for x in range(get_nb_nodes(f)):
        amatrix.append([])
        for y in range(get_nb_nodes(f)):
            amatrix[x].append(0)
    print("matrice allouée")
    newnode1 = -1
    row = 0
    nb_line = 0
    for line in file:
        if nb_line >= 4:
            pairofnode = line.split()
            newnode1 = pairofnode[0]
            newnode2 = pairofnode[1]
            amatrix[newnode1][newnode2] = 1
            nb_line = nb_line + 1

    file.close()
    return amatrix

def adjacency_list(f):
    file = open(f, "r")
    Alist = dict()
    i = 0
    for line in file:
        if (i >= 4):
            pairofnode = line.split()
            newnode1 = pairofnode[0]
            newnode2 = pairofnode[1]
            if(int(newnode1) in Alist):
                Alist.get(int(newnode1)).append(newnode2)
            else:
                Alist[int(newnode1)] = [newnode2]
            if (int(newnode2) in Alist):
                Alist.get(int(newnode2)).append(newnode1)
            else:
                Alist[int(newnode2)] = [newnode1]
        i = i + 1
    return Alist

def BFS(f):
    list_edges = list_of_edges(f)
    Alist = adjacency_list(f)
    q = queue.Queue()
    node_u, node_v  = list_edges[0]
    q.put((node_u))
    marked = set()
    marked.add(node_u)

    while ( q.not_empty):
        u = q.get()
        print(u)
        for v in Alist[int(u)]:
            if (not( q in marked)):
                q.put(v)
                marked.add(v)



#list_triangles
def listing_triangles(f):
    Alist = adjacency_list(f)
    triangles_list = []
    tsl = dict()
    list_nodes = []
    list_edges = list_of_edges(f)

    for u in Alist.keys():
        tsl[u] = sorted([w for w in Alist[u] if int(u) < int(w)])

    for e in list_edges:
        node_u, node_v = e
        w_set = set(tsl[int(node_u)]).intersection(set(tsl[int(node_v)]))
        for node_w in w_set:
            triangles_list.append((node_u,node_v,node_w))
    #return triangles_list
    return len(triangles_list)


for graphe in liste_graphes:


    list_edges = list_of_edges(graphe)
    adj_list = adjacency_list(graphe)
    adj_matrix = adjacency_matrix(graphe)
    print(list_edges, adj_list, adj_matrix)
    print("number of nodes " , get_nb_nodes(graphe))
    print("number of edges ", get_nb_edges(graphe))
    
     t1 = time.process_time()
     BFS(graphe)
     t2 = time.process_time()
     temps = t2 - t1

     print("calcul de complexité de l'algorithme BFS", temps)
     
    t1 = time.process_time()
    print(listing_triangles(graphe))
    t2 = time.process_time()
    temps = t2 - t1

    print("calcul de complexité de listing triangles", temps)
    

t1 = time.process_time()
print(listing_triangles(graphe))
t2 = time.process_time()
temps = t2 - t1
"""

BFS(f1)
#print(listing_triangles(f1))

