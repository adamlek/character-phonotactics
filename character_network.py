#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 17:15:34 2017

@author: adam
"""
import networkx as nx


file = '/home/adam/efselab/outp/rodarummet.tok'

G = nx.DiGraph()
edges = []

def char_grams(file, k):
    with open(file) as f:
        for ln in f:
            charlist = [x.lower() for x in ln.rstrip()]
            if not charlist:
                continue
            for i, w in enumerate(charlist):
                if not w.isalpha():
                    continue
                else:
                    for n in range(1,k+1):
                        try:
                            edges.append((w, charlist[i+n]))
                        except:
                            pass
    return edges

def create_graph(edges):
    for v1, v2 in edges:
        if v1 not in G.nodes():
            G.add_node(v1)
        if v2 not in G.nodes():
            G.add_node(v2)
    
        if G.has_edge(v1,v2):
            G[v1][v2]['weight'] += 1
        else:
            G.add_edge(v1,v2,weight=1)
    
    nx.write_gexf(G, 'chars.gexf')

if __name__ == '__main__':
    edges = char_grams(file, 2)
    create_graph(edges)