import  matplotlib
import statistics
#EX1

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


def node_min_degree(alist):

    min_deg = len(alist.get(1))
    index_of_min = 0
    for i in alist.keys():
        if( len(alist[i]) < min_deg):
            min_deg = len(alist[i])
            index_of_min = i
    return index_of_min


def k_core_decomp(G):
    i = get_nb_nodes(G)
    c = 0
    heta = dict()
    Alist = adjacency_list(G)
    avance = 0
    avancedelta = 1
    while (list(Alist.keys())) :
        v = node_min_degree(Alist)
        c = max(c, len(Alist[v]))

        Alist.pop(v)
        heta[v] = (i, c )   #correspond à l'ordre de parcours des noeuds et au core value
        i = i - 1
    return heta



#EX2

def graph_mining():
    id_file = open("ID.txt", "r")
    net_file = open("net.txt", "r")
    obj = []
    for line in id_file:
        pairID = line.split()

    for line in net_file:
        pairofnode = line.split()

    matplotlib.plot('Degree', 'Coreness', data=obj)

f1 = "C:/Users/Centaure Emeline/PycharmProjects/RESSOURCES/graphes/com-amazon.ungraph.txt"
f2 = "C:/Users/Centaure Emeline/PycharmProjects/RESSOURCES/graphes/com-lj.ungraph.txt"
f3 = "C:/Users/Centaure Emeline/PycharmProjects/RESSOURCES/graphes/com-orkut.ungraph.txt"


#id_file_friendster = open("graphes\com-lj.ungraph.txt", "r")

liste_graphes = [f1,f2,f3]



for graphe in liste_graphes:

    alist = adjacency_list(graphe)
    avg_degree_density =  get_nb_nodes(graphe)/get_nb_edges(graphe)
    print(  "average degree density : ", avg_degree_density )
    heta = k_core_decomp(graphe)
    print("core value of the graph ", max(heta.values()) )
    graph_mining(graphe)
