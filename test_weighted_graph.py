from weighted_graph import WeightedGraph, Node
import pytest


@pytest.fixture
def gimme_a_graph():
    nodes = [Node(5), Node("Bananas"),
             Node(3.2), Node(Node("what"))]
    graph = WeightedGraph(nodes)
    graph.add_edge(nodes[0], nodes[1], 10)
    graph.add_edge(nodes[0], nodes[2], 8)
    graph.add_edge(nodes[2], nodes[1], 11)
    graph.add_edge(nodes[1], nodes[3], 15)
    graph.add_edge(nodes[3], nodes[2], 4)
    graph.add_edge(nodes[3], nodes[0], 9)
    return graph, nodes


def test_depth_first(gimme_a_graph):
    g, nodes = gimme_a_graph
    n = Node("Nope")
    g.add_node(n)
    g.add_edge(n, g.nodes()[3])
    l = g.depth_first_traversal(g.nodes()[0])
    assert n not in l
    assert l[0] == g.nodes()[0]
    assert l[1] == g.nodes()[1]
    assert l[2] == g.nodes()[3]


def test_breadth_first(gimme_a_graph):
    g, nodes = gimme_a_graph
    n = Node("Nope")
    g.add_node(n)
    g.add_edge(n, g.nodes()[3])
    l = g.breadth_first_traversal(g.nodes()[0])
    assert n not in l
    assert l[0] == g.nodes()[0]
    assert l[1] == g.nodes()[1]
    assert l[2] == g.nodes()[2]


def test_weights(gimme_a_graph):
    g, nodes = gimme_a_graph
    x = g.edges()
    assert x[0][2] == 10
    assert x[1][2] == 8


def test_dijkstra(gimme_a_graph):
    g, nodes = gimme_a_graph
    g.dijkstra(nodes[0], nodes[3]) is [nodes[0], nodes[1], nodes[3]]


def test_bellamford(gimme_a_graph):
    g, nodes = gimme_a_graph
    g.bellamford(nodes[0], nodes[3]) is [nodes[0], nodes[1], nodes[3]]
