#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 17:15:34 2017

@author: adam
"""
import networkx as nx
from toolz import sliding_window

def ch_grams(fl):
    with open(fl) as f:
        data = ''.join([x.lower() for x in f.read().split('\n') if x])
    return list(sliding_window(2,data))


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
    fl = '/home/usr1/git/strindberg/data/pos_tagged_text/samlade_verk_06/0_5_6__röda_rummet.tok'

    G = nx.DiGraph()
    edges = ch_grams(fl)
    create_graph(edges)
