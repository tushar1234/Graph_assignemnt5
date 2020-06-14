# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# =============================================================================

# =============================================================================
# =============================================================================
import csv
output = []
with open("DG-AssocMiner_miner-disease-gene_processed.tsv") as tsvfile:
    tsvreader = csv.reader(tsvfile, delimiter="\t")
    for line in tsvreader:
        if line[0] not in output: 
            output.append(line[0])
print(len(output))
# =============================================================================

import networkx as nx
fh=open("DG-AssocMiner_miner-disease-gene_processed.tsv", 'rb')
#G=nx.read_edgelist(fh)
G=nx.read_edgelist(fh)
#  fh.close()
#  print(G.number_of_nodes())
#  #print(G.out_degree(0))
#  #print("diameter: %d" % nx.diameter(G))
#  # =============================================================================
#  # innode = []
#  # outnode = []
#  # for v in G.nodes():
#  #     if G.in_degree(v) == 0:
#  #         outnode.append(v)
#  #     else:
#  #         innode.append(v)
#  # =============================================================================
# =============================================================================
# #print("No of Disease nodes: " + str(len(outnode)))
# #print("No of Gene nodes: " + str(len(innode)))
# #largest = max(nx.strongly_connected_components(G), key=len)
# #Gc = max(nx.weakly_connected_component_subgraphs(G), key=len)
# #print(Gc.number_of_nodes())
# =============================================================================
# bunch = []
# x = output.pop()
# while len(output) > 0:
#     y = output.pop()
#     tup = (x,y)
#     bunch.append(tup)
#     x = y
# print(len(bunch))
# preds = nx.jaccard_coefficient(G, bunch)
# 
# tup = []
# for u, v, p in preds:
#     t = (p,u,v)
#     tup.append(t);
# print(len(tup))
# tup.sort(key = lambda x: float(x[0]), reverse = True) 
# 
# i=0
# for a,b,c in tup:
#     i = i+1
#     print(a,b,c)
#     if i == 20:
#         break
# =============================================================================
# =============================================================================
# node = []
# while len(output) > 0:
#     y = output.pop()
#     node.append(y)
#     
# print(len(node))
# =============================================================================

s = nx.simrank_similarity(G, output[0], output[1])
print(s)
#f = open('resul7.txt', 'w')
#f.write(str(s))
#f.close
# =============================================================================
# for x in node:
#     print(x)
#     print(s[x])
# =============================================================================
print("sim")



