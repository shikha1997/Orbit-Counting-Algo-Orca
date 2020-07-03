# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 14:20:08 2019

@author: User
"""
import networkx as nx
import numpy as np
import pandas as pd
import random 

abc = nx.read_edgelist("data/bio-pathways-network.edgelist", nodetype = int, edgetype = int)
di = {}
new_lab = [i for i in range(0, 21557)]
mapping = dict(zip(abc, new_lab))



df=pd.read_csv("C:/Users/User/Desktop/internship/5graphlets.txt",delimiter=" ",header=None)

ids=list(mapping.keys())
df.insert(loc=0, column='ids', value=ids)

disease_proteins=[10736, 1191, 120237, 1270, 1387, 1471, 1509, 1639, 170825, 2251, 2326, 2353, 2554, 2637, 2664, 2670, 27040, 283, 2892, 3297, 331, 340990, 3718, 3727, 3797, 3949, 4744, 5154, 5179, 5444, 5630, 598, 6256, 6404, 6464, 6615, 6647, 682, 7074, 7090, 7114, 7124, 7431, 7476, 794, 834, 9118, 924, 968] 

df_dp=df[(df['ids'].isin(disease_proteins))]
df_dp.set_index('ids',inplace=True)


test_sum=list(df_dp.sum(axis=0))

coln=[]
for i in range(73):
    coln.append(i)
val_df=pd.DataFrame(columns=coln)

for i in range(5000):
    temp=df[(df['ids'].isin(random.sample(ids,47)))]
    temp.set_index('ids',inplace=True)
    temp1=list(temp.sum(axis=0))
    val_df.loc[i]=temp1

sort_val=pd.DataFrame(np.sort(val_df.values,axis=0) ,columns=val_df.columns)
last_50=sort_val.iloc[-50:]

##CALCULATING SIGNIFICANT ORBITS
sign_check=[]
sign_orbits=[]
for i in range(73):
    if(test_sum[i] in range(last_50.loc[4950,i],last_50.loc[4999,i])):
        sign_check.append(1)
        sign_orbits.append(i)
    else:
        sign_check.append(0)

#print(sort_val[sort_val[0]==test_sum[0]].index.values)
#print(sort_val[0].sub(test_sum[0]).abs().idxmin())

p_values=[]        
for i in range(73):
    if(test_sum[i] <= sort_val.loc[0,i]):
        p_values.append(1)
    elif(test_sum[i]>=sort_val.loc[4999,i]):
        p_values.append(0)
    else:
        norm=(4999-(sort_val[i].sub(test_sum[i]).abs().idxmin()))/5000
        p_values.append(norm)
    
        


    
   

#print(test_sum[0] in range(last_50.loc[4950,0],last_50.loc[4999,0]) ) 