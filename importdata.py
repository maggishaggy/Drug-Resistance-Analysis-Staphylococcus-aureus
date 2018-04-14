# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 12:15:03 2018

@author: Manik Sharma
"""
import networkx as nx
import operator

def get_protein_list(label):
    s=''
    ret=[]
    
    file={'target':['database/Drug Target and Resistant Protein - Sheet1.csv',1],'resistance':['database/Resistance Proteins - Sheet1.csv',0]}
    
    with open(file[label][0]) as f:
        s=f.readline()
#        print (s)
        while True:
            s=f.readline()
            if s=='':
                break
            g=s.strip().split(',')
#            print (g)
            pro=g[file[label][1]]
            if len(pro)!=0:
                ret.append(pro)
    
    return ret



target=get_protein_list('target')
resistance=get_protein_list('resistance')

G=nx.Graph()

s=''
c=0
with open('database/93062.protein.links.detailed.v10.5.txt') as f:
    s=f.readline()
#    print (s)
    while True:
        s=f.readline()
        if s=='':
            break
        g=s.strip().split()
        if int(g[9])>0:
            G.add_edge(g[0],g[1])
    
print (len(G.edges()),len(G.nodes()))

def rank(dic,n):
    sorted_dic = sorted(dic.items(), key=operator.itemgetter(1))
#    sorted_dic.reverse()
    return(sorted_dic[:n])

#print (rank(nx.betweenness_centrality(G),10))

#print (list(G.nodes())[:5])
    

    
cen_mes = nx.edge_betweenness_centrality(G)
nx.set_edge_attributes(G, cen_mes , 'betweenness')

tar_res_len={}

for t in target:
    for r in resistance:
        if t not in G.nodes() or r not in G.nodes():
            continue
        else:
            try:
                tar_res_len[(t,r)]=nx.shortest_path(G,t,r,'betweeness')
            except nx.NetworkXNoPath:
                tar_res_len[(t,r)]=float('nan')
        
print (tar_res_len)
        