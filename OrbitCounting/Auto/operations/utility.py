import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

EDGELIST_FILE = "data/bio-pathways-network.edgelist"
ppi = nx.read_edgelist(EDGELIST_FILE, nodetype = int)

def actual_disease_protein(raw_disease_proteins):
    global ppi
    disease_proteins = []
    for di_pr in raw_disease_proteins:
        if ppi.has_node(di_pr):
            disease_proteins.append(di_pr)
    return (sorted(disease_proteins))


def get_the_edges(protein):
    global ppi

    return (ppi.edges(protein))

def disease_disease_interation(dictionary, disease_proteins):
    global ppi
    list_of_disease_proteins_its_connected = {}
    for a in dictionary.keys():
        b = 0
        list_of_disease_proteins_its_connected[a] = []
        for i in disease_proteins:
            if ppi.has_edge(a, i):
                b += 1
                list_of_disease_proteins_its_connected[a].append(i)
    return list_of_disease_proteins_its_connected


def longest_component(dictionary_with_disease_disease_interation):
    protein_code, number_of_edges = 0, 0
    a_dict = {}
    for a in dictionary_with_disease_disease_interation.keys():
        if len(dictionary_with_disease_disease_interation[a]) > number_of_edges:
            number_of_edges = len(dictionary_with_disease_disease_interation[a])
            protein_code = a
            a_dict[a] = dictionary_with_disease_disease_interation[a]
    if number_of_edges > 1:
        return protein_code, number_of_edges

    else:
        temp_list = []
        for a in a_dict:
            if a_dict[a] == a:
                continue
            else:
                temp_list.append(a)
                temp_list.append(len(a_dict[a]))

        if len(temp_list) == 0:
            return protein_code, number_of_edges
        else:
            return temp_list[0], temp_list[1]


def connect_disease_proteins(list_of_disease_proteins):
    global ppi
    di = {}
    for i in list_of_disease_proteins:
        di[i] = []
        for j in list_of_disease_proteins:
            if j == i:
                continue
            try:
                path = nx.shortest_path(ppi, i, j)
                if nx.shortest_path_length(ppi, i, j) == 1:
                    di[i].append(j)
                for k in range(1, len(path) - 1):
                    if not (path[k] in di):
                        di[path[k]] = []

                    di[path[k]].append(path[k + 1])
            except:
                continue
    return di


def plot_graph(disease_proteins):
    dictionary_to_be_graphed = connect_disease_proteins(disease_proteins)
    a_graph = nx.Graph(dictionary_to_be_graphed)
    node_color = []
    node_size = []
    edge_color = []
    width = []
    for node in a_graph.nodes():
        if node in disease_proteins:
            node_color.append("red")
            node_size.append(20)
        else:
            node_color.append("blue")
            node_size.append(5)

    for edge in a_graph.edges():
        if(edge[0] in disease_proteins) and (edge[1] in disease_proteins):
            edge_color.append("yellow")
            width.append(2)
        else:
            edge_color.append("black")
            width.append(1)
    nx.draw(a_graph, node_size = node_size, node_color = node_color, edge_color = edge_color, width = width)
    plt.show()
   


def plot_for_the_gene(gene_id):
    global ppi
    dictionary = {}
    dictionary[gene_id] = [j for i, j in ppi.edges(gene_id)]
    gr = nx.Graph(dictionary)
    nx.draw(gr)
    plt.show()
