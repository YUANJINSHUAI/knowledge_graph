# -*- coding: utf-8 -*-
# Created by yuanjinshuai at 2019-08-06

import pandas as pd
import datetime
import networkx as nx
import json
from networkx.readwrite import json_graph
import math

flow_data = pd.read_excel('./datasets/region_industry_data.xlsx')
reason_data = pd.read_excel('./datasets/region_industry_reason.xlsx')

region_list = ['设计企业创意园（CDD港）', '服装文化创意园', '建筑和工程设计园', '博洛尼都市工业设计园', '亦庄西曼工业设计园']
G1 = nx.DiGraph()
# add node
for p in region_list:
    G1.add_node(p, label=p, ws=100, ntype='main')  # row:68 means2018

# add edges between regions
for i in region_list:
    for j in region_list:
        if type(flow_data[flow_data.流入地区_下_流出地区_右 == i][j].values[0]) is str:
            continue
        if i != j:
            G1.add_edge(i, j, label='从%s流入%s' % (i, j),
                        weight=flow_data[flow_data.流入地区_下_流出地区_右 == i][j].values[0], type='flow')

# add top5reason to nodes
for region in region_list:
    for i in range(5):  # top5
        if type(reason_data[reason_data.地区 == region].values[0][i+1]) is float:
            break
        G1.add_node(region+'_'+reason_data[reason_data.地区 == region].values[0][i+1],
                    label=reason_data[reason_data.地区 == region].values[0][i+1], ws=10, ntype='sub')
        G1.add_edge(region+'_'+reason_data[reason_data.地区 == region].values[0][i+1], region,
                    weight=10, type='reason')

""" Write to GEXF """
# Use 1.2draft so you do not get a deprecated warning in Gelphi
nx.write_gexf(G1, "./output/region_industry_network.gexf", version="1.2draft")
# nx.write_gexf(G1, "./output/jin_jing_ji_city_network.gexf", version="1.2draft")

# with open('networkdata1.json', 'w') as outfile1:
#     outfile1.write(json.dumps(json_graph.node_link_data(G1)))
#
# data = json_graph.node_link_data(G1)
#
# font: {
#         size: 100,
#         strokeColor: '#fff',
#         strokeWidth: 5
#       }
