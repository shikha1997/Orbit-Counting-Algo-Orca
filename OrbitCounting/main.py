#import networkx as nx
import matplotlib.pyplot as plt
g=nx.read_edgelist('gr.txt',create_using=nx.Graph(),nodetype=int)
print(nx.info(g))

with open('C:/Users/User/Desktop/internship/gr.txt','r') as f:
    with open('C:/Users/User/Desktop/internship/rr.txt','w') as g:
        for line in f:
            x,y=line.split()
            a=int(x)
            b=int(y)
            if(a and b) in ran_nodes:
                g.writelines(line)
            
