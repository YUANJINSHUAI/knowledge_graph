# -*- coding: utf-8 -*-
# Created by yuanjinshuai at 2019-08-06

import pandas as pd
import networkx as nx
import datetime

flow_data = pd.read_excel('./datasets/population_data.xlsx')
gdp_data = pd.read_excel('./datasets/gdp.xlsx')
reason_data = pd.read_excel('./datasets/reason.xlsx', index_col='省份')

# transpose reason_data
reason_data = reason_data.transpose()

#jcity_list = ['北京', '天津', '河北']
city_list = ['江苏', '上海', '浙江']
G1 = nx.DiGraph()
# add node
for p in city_list:
    G1.add_node(p, label=p, ws=gdp_data[gdp_data.年 == datetime.datetime(2017, 12, 31, 0, 0)][p+':GDP'].values[0],
                ntype='main')  # row:68 means2018
    print('流动当年%s的GDP:%s' % (p, gdp_data[gdp_data.年 == datetime.datetime(2017, 12, 31, 0, 0)][p+':GDP'].values[0]))

# add edges between cities
count = 0
for i in city_list:
    for j in city_list:
        if i != j:
            G1.add_edge(i, j, label='从'+i+'流入'+j,
                        weight=flow_data[flow_data.流入省份_下_流出省份_右 == j][i].values[0], type_='flow')  # i：流出省份，j：流入省份
            print('从%s流入%s的人数:%s人' % (i, j, flow_data[flow_data.流入省份_下_流出省份_右 == j][i].values[0]))

# add top5reason to nodes
for city in city_list:

    city_reason_data = reason_data[city].sort_values(ascending=False)
    print('目前看的是:%s' % city)
    for i in range(5):  # top5
        G1.add_node(city+'_'+city_reason_data.index[i], label=city_reason_data.index[i], ws=city_reason_data[i],
                    ntype='sub')
        G1.add_edge(city+'_'+city_reason_data.index[i], city, label=city+'_'+city_reason_data.index[i],
                    weight=city_reason_data[i], type_='reason')  # i：流出省份，j：流入省份
        print('流入%s的人中有%s人%s' % (city, city_reason_data[i], city_reason_data.index[i]))


""" Write to GEXF """
# Use 1.2draft so you do not get a deprecated warning in Gelphi
nx.write_gexf(G1, "./output/chang_san_jiao_city_network.gexf", version="1.2draft")



