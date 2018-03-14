# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 12:15:03 2018

@author: Manik Sharma
"""
import networkx as nx
import operator

G=nx.Graph()

s=''
c=0
with open('93062.protein.links.detailed.v10.5.txt') as f:
    s=f.readline()
    print (s)
    while True:
        s=f.readline()
        if s=='':
            break
        g=s.strip().split()
        G.add_edge(g[0],g[1])
    
print (len(G.nodes()))

def rank(dic,n):
    sorted_dic = sorted(dic.items(), key=operator.itemgetter(1))
    sorted_dic.reverse()
    return(sorted_dic[:n])

#print (rank(nx.betweenness_centrality(G),10))

print (list(G.nodes())[:5])