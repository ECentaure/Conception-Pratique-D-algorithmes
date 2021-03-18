import networkx as nx
import random
import time
import collections
from random import seed
from random import random
import matplotlib.pyplot as plt

#EX1 Simple Benchmark



nb_nodes = 400
palette_couleur= ['blue', 'green' ,'yellow', 'red' ]
color_map = []
nb_cluster = 4
size_cluster = int(nb_nodes / nb_cluster)

p = random()
q = random() % p

G = nx.Graph()

list_cluster = []

def rand_in_cluster(G,list_clust):
    indice_random = random()*len(list_clust) % len(list_cluster)
    j =  list_cluster[int(indice_random)]
    G.add_edge(i, j)

def union_list(list_of_list):
    final_list = []
    for liste in list_of_list:
        final_list = final_list + liste
    return final_list

for x in range(nb_cluster):
    list_cluster.append(nx.Graph())

    for i in range(size_cluster*x , size_cluster*(x+1)):
        list_cluster[x].add_node(i)
        color_map.append(palette_couleur[x])
for x in range(nb_cluster):
    print(list_cluster[x].number_of_nodes())

for x in range(nb_cluster):
    G.add_nodes_from(list_cluster[x])



for x in range(nb_cluster):
    for i in range(size_cluster):
        for j in range(i, size_cluster):
            if (random() < p ):
                list_cluster[x].add_edge(i,j)
            #if (random() < q):
                #rand_in_cluster(G,union_list([list_cluster[ -x : -x + len(list_cluster)]]))

print(G.number_of_nodes())

nx.draw_spring(G,node_color=color_map,with_labels=True)
plt.show()
#EX2 Label Propagation



def label_propagation(G):
    print("label propagation")
    list_random_order = []
    for node in G.nodes():
        G.nodes[i]['label'] = i
        for voisin in G.adj[i]:
            frequence_label_voisins = collections.Counter(G.adj[i])
            G.nodes[i]['label'] = max(frequence_label_voisins)


#EX3 nex algorithm
# n°1
def comm_detect(G):
    print("community detection")
# n°2

def my_coom_detect(G):
    print("community detection")

#EX4 Experimental evaluation
def experimental_eval(liste_graphes):

    for g in liste_graphes:
        print("calcul de complexité de l'algorithme Label Propagation")
        t1 = time.process_time()
        label_propagation(g)
        t2 = time.process_time()
        temps_lab_prop = t2 - t1

        print("calcul de complexité de l'algorithme de Louvain")


        t1 = time.process_time()


        t2 = time.process_time()
        temps_louvain = t2 - t1
        print("calcul de complexité de l'algorithme proposé EXO3")

        t1 = time.process_time()
        comm_detect(g)
        t2 = time.process_time()
        temps_ALGO3 = t2 - t1

        print("temps d'execution pour l'algorithme Label propagation  " , temps_lab_prop)
        print("temps d'execution pour l'algorithme de Louvain  " , temps_louvain)
        print("temps d'execution pour l'algorithme de l'exo 3  " , temps_ALGO3)


experimental_eval([G])