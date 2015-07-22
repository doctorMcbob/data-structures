from graphtraversal import SimpleGraph, Node
import pytest


@pytest.fixture
def gimme_a_graph():
    nodes = [Node(5), Node("Bananas"),
             Node(3.2), Node(Node("what"))]
    graph = SimpleGraph(nodes)
    graph.add_edge(nodes[0], nodes[1])
    graph.add_edge(nodes[0], nodes[2])
    graph.add_edge(nodes[2], nodes[1])
    graph.add_edge(nodes[1], nodes[3])
    graph.add_edge(nodes[3], nodes[2])
    graph.add_edge(nodes[3], nodes[0])
    return graph


def test_depth_first(gimme_a_graph):
    g = gimme_a_graph
    n = Node("Nope")
    g.add_node(n)
    g.add_edge(n, g.nodes()[3])
    l = g.depth_first_traversal(g.nodes()[0])
    assert n not in l
    assert l[0] == g.nodes()[0]
    assert l[1] == g.nodes()[1]
    assert l[2] == g.nodes()[3]


def test_breadth_first(gimme_a_graph):
    g = gimme_a_graph
    n = Node("Nope")
    g.add_node(n)
    g.add_edge(n, g.nodes()[3])
    l = g.breadth_first_traversal(g.nodes()[0])
    assert n not in l
    assert l[0] == g.nodes()[0]
    assert l[1] == g.nodes()[1]
    assert l[2] == g.nodes()[2]
