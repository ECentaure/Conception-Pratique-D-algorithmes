import numpy as np
import matplotlib

file1 = "C:/Users/Centaure Emeline/PycharmProjects/TME1_CPA/RESSOURCES/alr21--dirLinks--enwiki-20071018.txt"
file2 = "C:/Users/Centaure Emeline/PycharmProjects/TME1_CPA/RESSOURCES/alr21--pageNum2Name--enwiki-20071018.txt"

#h
#test1

def get_nb_nodes(f) :
    file_to_read = open(f, "r")
    nb_line = 0
    nb_nodes = 0
    set_nodes = set()
    for line in file_to_read:
        if nb_line >= 5:
            p = line.split()
            if p[0] not in set_nodes:
                set_nodes.add(p[0])
                nb_nodes = nb_nodes + 1
            if p[1] not in set_nodes:
                set_nodes.add(p[1])
                nb_nodes = nb_nodes + 1
        nb_line = nb_line + 1

    return nb_nodes

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

def transitionMatrix (graph):
    print("test")
    n = get_nb_nodes(graph)
    matrice = np.zeros((n,n))
    #for edges in list_edges:

#EX1 pageRank
def pageRank(graphe_G , t, alpha ):
    n = get_nb_nodes(graphe_G)
    Transformation_matrix = transitionMatrix(graphe_G)
    I_matrix = (1/n) * np.multiply(np.identity(n), (1/n) )
    P_matrix =  (1/2) * I_matrix

    for i in range(0,t):
        P_matrix = P_matrix.dot(Transformation_matrix)
        P_matrix = np.multiply( P_matrix, (alpha - 1) * alpha)
        P_matrix = np.multiply(P_matrix, I_matrix)

    return P_matrix

"""
#EX2 Correlations
def d_in(nodes):
    

def d_out(nodes):


def correlation(graphe_G):

    coord_1X = []
    coord_1Y = []
    coord_2X = []
    coord_2Y = []
    coord_3X = []
    coord_3Y = []
    coord_4X = []
    coord_4Y = []

 :
        coord_1X = pageRank( , , 0.15)
        coord_1Y = d_in(node)
        coord_2X = pageRank( , , 0.15)
        coord_2Y = d_out(node)
        coord_3X = pageRank( , , 0.15)
        coord_3Y = pageRank( , , 0.1)
        coord_4X = pageRank( , , 0.15)
        coord_4Y = pageRank( , , 0.2)
        coord_5X = pageRank( , , 0.15)
        coord_5Y = pageRank( , , 0.5)
        coord_6X = pageRank( , , 0.15)
        coord_6Y = pageRank( , , 0.9)

    matplotlib.pyplot.scatter(coord_1X, coord_1Y, c = 'red')
    matplotlib.pyplot.scatter(coord_2X, coord_2Y, c='blue')
    matplotlib.pyplot.scatter(coord_3X, coord_3Y, c='green')
    matplotlib.pyplot.scatter(coord_4X, coord_4Y, c='yellow')
    matplotlib.pyplot.scatter(coord_5X, coord_5Y, c='brown')
    matplotlib.pyplot.scatter(coord_6X, coord_6Y, c='black')
"""
print(get_nb_nodes(file1))
pageRank( file1 , 2, 0.15)

#EX3 Personalized PageRank