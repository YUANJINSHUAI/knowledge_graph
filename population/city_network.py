# -*- coding: utf-8 -*-
# Created by yuanjinshuai at 2019-08-06

import pandas as pd
import networkx as nx
import datetime

flow_data = pd.read_excel('./datasets/population_data.xlsx')
gdp_data = pd.read_excel('./datasets/gdp.xlsx')

jing_jin_ji_list = ['北京', '天津', '河北']
G1 = nx.Graph()
# add node
for p in jing_jin_ji_list:
    G1.add_node(p, label=p, ws=gdp_data[gdp_data.年 == datetime.datetime(2017, 12, 31, 0, 0)][p+':GDP'].values[0],
                ntype='main')  # row:68 means2018
    print('流动当年%s的GDP:%s' %(p, gdp_data[gdp_data.年 == datetime.datetime(2017, 12, 31, 0, 0)][p+':GDP'].values[0]))

# add edges between cities
for i in jing_jin_ji_list:
    for j in jing_jin_ji_list:
        if i != j:
            G1.add_edge(i, j, label='从'+i+'流入'+j,
                        weight=flow_data[flow_data.流入省份_下_流出省份_右 == j][i].values[0])  # i：流出省份，j：流入省份
            print('从%s流入%s的人数:%s人' % (i, j, flow_data[flow_data.流入省份_下_流出省份_右 == j][i].values[0]))

""" Write to GEXF """
# Use 1.2draft so you do not get a deprecated warning in Gelphi
nx.write_gexf(G1, "./output/city_network.gexf", version="1.2draft")



