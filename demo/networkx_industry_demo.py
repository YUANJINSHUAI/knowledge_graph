# -*- coding: utf-8 -*-
# Created by yuanjinshuai at 2019-08-02

import networkx as nx
""" Create a graph with three nodes"""
G = nx.DiGraph()

# add company node
G.add_node('百度', ws=445.16, ntype='main')
G.add_node('小米', ws=199.05, ntype='main')
G.add_node('图灵机器人', ws=1.44, ntype='main')
G.add_node('搜狗', ws=15.15, ntype='main')

# add attribute node
G.add_node('百度_智能家居', label='智能家居', ws=1, ntype='sub')
G.add_node('小米_智能家居', label='智能家居', ws=1, ntype='sub')
G.add_node('图灵机器人_智能家居', label='智能家居', ws=1, ntype='sub')
G.add_node('搜狗_智能家居', label='智能家居', ws=1, ntype='sub')


# add different color to node
for item in G.nodes(data=True):
    if item[1]['ntype'] == 'main':
        G.node[item[0]]['viz'] = {'color': {'r': 255, 'g': 0, 'b': 0, 'a': 0}}
    elif item[1]['ntype'] == 'sub':
        G.node[item[0]]['viz'] = {'color': {'r': 0, 'g': 255, 'b': 0, 'a': 0}}

# add edge between nodes
G.add_edge('百度', '百度_智能家居',  label='attribute', weight=2)
G.add_edge('小米_智能家居', '小米', label='attribute', weight=2)
G.add_edge('图灵机器人_智能家居', '图灵机器人', label='attribute', weight=2)
G.add_edge('搜狗_智能家居', '搜狗', label='attribute', weight=2)


""" Write to GEXF """
# Use 1.2draft so you do not get a deprecated warning in Gelphi
nx.write_gexf(G, "./output/file1.gexf", version="1.2draft")
