import  matplotlib

#EX1


def get_nb_nodes(f) :
    file_to_read = f
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
    f.seek(0)
    return nb_nodes

def node_min_degree(G):
    min_deg = G.degree[0]
    index_of_min = 0
    for i in range (0, G.size()):
        if( G.degree[i] < min_deg):
            min_deg = G.degree[i]
            index_of_min = i
    return index_of_min


def k_core_decomp(G):
    i = get_nb_nodes(G)
    c = 0
    while (list(G.nodes)) :
        v = node_min_degree(G)
        c = max(c, G.degree[node_min_degree()])
        G.remove_node(v)
        G.remove_edge()
        G[v]['ordre'] = i    #correspond au "heta"
        i = i - 1




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



id_file_amazon = open( "C:/Users/Centaure Emeline/PycharmProjects/TME1_CPA/RESSOURCES/graphes/com-amazon.ungraph.txt", "r")
id_file_liveJournal = open("C:/Users/Centaure Emeline/PycharmProjects/TME1_CPA/RESSOURCES/graphes/com-lj.ungraph.txt", "r")
id_file_orkut = open("C:/Users/Centaure Emeline/PycharmProjects/TME1_CPA/RESSOURCES/graphes/com-orkut.ungraph.txt", "r")
#id_file_friendster = open("graphes\com-lj.ungraph.txt", "r")

liste_graphes = [id_file_amazon,id_file_liveJournal,id_file_orkut]

for graphe in liste_graphes:
    k_core_decomp(graphe)
    graph_mining(graphe)