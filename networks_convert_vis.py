from itertools import chain
import json
import networkx as nx


_attrs = dict(id='id', source='source', target='target', key='key')


# This is stolen from networkx JSON serialization. It basically just changes what certain keys are.
def node_link_data(G, attrs=_attrs):
    """Return data in node-link format that is suitable for JSON serialization
    and use in Javascript documents.

    Parameters
    ----------
    G : NetworkX graph

    attrs : dict
        A dictionary that contains four keys 'id', 'source', 'target' and
        'key'. The corresponding values provide the attribute names for storing
        NetworkX-internal graph data. The values should be unique. Default
        value:
        :samp:`dict(id='id', source='source', target='target', key='key')`.

        If some user-defined graph data use these attribute names as data keys,
        they may be silently dropped.

    Returns
    -------
    data : dict
       A dictionary with node-link formatted data.

    Raises
    ------
    NetworkXError
        If values in attrs are not unique.

    Examples
    --------
    >>> from networkx.readwrite import json_graph
    >>> G = nx.Graph([(1,2)])
    >>> data = json_graph.node_link_data(G)

    To serialize with json

    >>> import json
    >>> s = json.dumps(data)

    Notes
    -----
    Graph, node, and link attributes are stored in this format. Note that
    attribute keys will be converted to strings in order to comply with
    JSON.

    The default value of attrs will be changed in a future release of NetworkX.

    See Also
    --------
    node_link_graph, adjacency_data, tree_data
    """
    multigraph = G.is_multigraph()
    id_ = attrs['id']
    source = attrs['source']
    target = attrs['target']
    # Allow 'key' to be omitted from attrs if the graph is not a multigraph.
    key = None if not multigraph else attrs['key']
    if len(set([source, target, key])) < 3:
        raise nx.NetworkXError('Attribute names are not unique.')
    data = {}
    data['directed'] = G.is_directed()
    data['multigraph'] = multigraph
    data['graph'] = G.graph
    data['nodes'] = [dict(chain(G.node[n].items(), [(id_, n), ('label', n)])) for n in G]
    if multigraph:
        data['links'] = [
            dict(chain(d.items(),
                       [('from', u), ('to', v), (key, k)]))
            for u, v, k, d in G.edges_iter(keys=True, data=True)]
    else:
        data['links'] = [
            dict(chain(d.items(),
                       [('from', u), ('to', v)]))
            for u, v, d in G.edges_iter(data=True)]
    return data


def main():
    graph = nx.Graph()
    graph.add_nodes_from([1, 2, 3, 4, 5])
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 4)
    graph.add_edge(2, 5)
    # You would pass in the following data into something that initializes the graph in visjs
    print(json.dumps({'nodes': node_link_data(graph)['nodes'], 'edges': node_link_data(graph)['links']}, indent=4))

if __name__ == "__main__":
    main()