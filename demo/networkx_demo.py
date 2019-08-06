# -*- coding: utf-8 -*-
# Created by yuanjinshuai at 2019-08-02

import networkx as nx
import pandas as pd
""" Create a graph with three nodes"""
G = nx.Graph()



G.add_node('red', ws =1.0, ntype='main')
G.add_node('green', ws=1.5, ntype='sub')
G.add_node('blue', ws=1.2, ntype='sub')



for item in G.nodes(data = True):
    if item[1]['ntype'] == 'main':
        G.node[item[0]]['viz'] = {'color': {'r': 255, 'g': 0, 'b': 0, 'a': 0}}
    elif item[1]['ntype'] == 'sub':
        G.node[item[0]]['viz'] = {'color': {'r': 0, 'g': 255, 'b': 0, 'a': 0}}

""" Write to GEXF """
# Use 1.2draft so you do not get a deprecated warning in Gelphi
nx.write_gexf(G, "file2.gexf", version="1.2draft")
