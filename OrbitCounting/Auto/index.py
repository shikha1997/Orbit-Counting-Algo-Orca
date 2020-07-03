import networkx as nx
abc = nx.read_edgelist("data/bio-pathways-network.edgelist", nodetype = int, edgetype = int)
di = {}
new_lab = [i for i in range(0, 21557)]
mapping = dict(zip(abc, new_lab))
abcd = nx.relabel_nodes(abc, mapping)
abcd.remove_edges_from(nx.selfloop_edges(abcd))
nx.write_edgelist(abcd, "relabel.txt")
