# -*- coding: utf-8 -*-
# Created by yuanjinshuai at 2019-08-05
import networkx as nx
import pandas as pd

G = nx.DiGraph()

raw_company_data = pd.read_excel('./datasets/company_data.xlsx')
raw_investment_data = pd.read_excel('./datasets/investment.xlsx')


# add company node
company_set = set()
for i in range(0, raw_company_data.shape[0]):
    if raw_company_data['公司'][i] not in company_set:
        G.add_node(raw_company_data['公司'][i], ws=raw_company_data['企业总资产（亿：美元）'][i], type='company')
        company_set.add(raw_company_data['公司'][i])
    else:
        continue

# add attribute node and their edges
for j in range(0, raw_company_data.shape[0]):
    if pd.isna(raw_company_data['小类'][j]):  # 小类为空
        G.add_node(raw_company_data['公司'][j] + '_' + raw_company_data['中类'][j],
                   label=raw_company_data['中类'][j], ws=1/4, type='attribute')
        G.add_edge(raw_company_data['公司'][j], raw_company_data['公司'][j] + '_' + raw_company_data['中类'][j], weight=4)
    else:
        G.add_node(raw_company_data['公司'][j] + '_' + raw_company_data['小类'][j],
                   label=raw_company_data['小类'][j], ws=1/4, type='attribute')
        G.add_edge(raw_company_data['公司'][j], raw_company_data['公司'][j] + '_' + raw_company_data['小类'][j], weight=4)

# add investment edgex
for k in range(0, raw_investment_data.shape[0]):
    G.add_edge(raw_investment_data['被投资公司'][k], raw_investment_data['投资公司'][k],
               label='投资'+str(raw_investment_data['投资规模（:亿美元）'][k])+'亿美元',
               weight=raw_investment_data['投资规模（:亿美元）'][k]*50)


nx.write_gexf(G, "./output/file1.gexf", version="1.2draft")

