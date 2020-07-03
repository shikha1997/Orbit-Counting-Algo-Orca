import operations.utility as utility
from collections import deque

class Disease_Protein():
    def __init__(self, disease_name, raw_disease_proteins):
        self.disease_name = disease_name
        self.disease_proteins = utility.actual_disease_protein(raw_disease_proteins)
        self.actual_disease_protein_size = len(raw_disease_proteins)
        self.dict_node_edge = {}
        self.disease_disease_interaction = {}
        self.longest_component = []
        self.size_of_largest_pathway_comp = 0
        self.dictionary_for_graph = {}
        self.all_single_components = []
        self.all_cluster_components = deque()
        self.clusters = {}

    def __str__(self):
        return (f'Disease Searched For: {(self.disease_name).upper()}')


    def build_dict_node_edge(self):
        for protein in self.disease_proteins:
            self.dict_node_edge[protein] = [y for x, y in utility.get_the_edges(protein)]


    def build_disease_disease_interaction_dict(self):
        self.disease_disease_interaction = utility.disease_disease_interation(self.dict_node_edge, self.disease_proteins)


    def size_of_largest_pathway_component(self):
        protein, num_edges = utility.longest_component(self.disease_disease_interaction)
        already_connected = self.disease_disease_interaction[protein]
        if (len(already_connected) == 1) and already_connected[0] == protein:
            self.size_of_largest_pathway_comp = len(already_connected) / len(self.disease_disease_interaction)

        else:
            for i in already_connected:
                if self.disease_disease_interaction[i]:
                    for val in self.disease_disease_interaction[i]:
                        if val not in already_connected:
                            already_connected.append(val)
            self.size_of_largest_pathway_comp = len(already_connected) / (self.actual_disease_protein_size)

        print(already_connected)
        if len(already_connected) == 1:
            self.all_single_components = self.disease_proteins

        else:
            for i in self.disease_disease_interaction:
                if self.disease_disease_interaction[i] == [] or self.disease_disease_interaction[i] == [i]:
                    self.all_single_components.append(i)
                else:
                    self.all_cluster_components.append(i)
            counter = 0
            while not (self.all_cluster_components == deque([])):
                node = self.all_cluster_components[0]
                li = deque()
                cluster_comp = []
                li.append(node)
                while not (li == deque([])):
                    for j in self.disease_disease_interaction[li[0]]:

                        if not (j in cluster_comp):
                            li.append(j)
                            cluster_comp.append(j)
                            try:
                                self.all_cluster_components.remove(j)
                            except:
                                continue

                    li.popleft()
                counter += 1
                self.clusters[f'cluster_{counter}'] = cluster_comp


    def graphing(self):
        utility.plot_graph(self.disease_proteins)


    def largest_pathway_comp(self):
        if len(self.clusters) > 0:
            length = 0
            output = []
            for i, j in self.clusters.items():
                if len(j) > length:
                    length = len(j)
                    output = j
            return (f"Largest Pathway Coponent: {output}")
        return (f"NO CLUSTERS FOUND.")


    def get_single_components(self):
        return (f"Disease Protein in Single Component: {self.all_single_components}")


    def get_clusters(self):
        if len(self.clusters) > 0:
            return (f"Disease Proteins in Largest Component: {self.clusters}")
        return (f"All Disease Proteins are Single Components.")


    def get_size_of_largest_pathway_component(self):
        return (f"Size of Largest Pathway Component: {self.size_of_largest_pathway_comp}")


    def build_essentials(self):
        self.build_dict_node_edge()
        self.build_disease_disease_interaction_dict()
        self.size_of_largest_pathway_component()
