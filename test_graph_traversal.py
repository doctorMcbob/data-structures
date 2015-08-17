from weighted_graph import Graph
#py.test -q test_graph_traversal.py 


def test_real_short():
    """
    Test with the shortest path having the lowest weight
    """
    g = Graph()
    g.add_node('a')
    g.add_edge('a', 'b', 9)
    g.add_edge('a', 'e', 3)
    g.add_edge('b', 'c', 6)
    g.add_edge('b', 'e', 9000)
    g.add_edge('c', 'd', 6)
    g.add_edge('e', 'c', 5)
    g.add_edge('e', 'd', 1)
    g.add_edge('e', 'f', 3)
    g.add_edge('f', 'a', 8)

    assert g.dijkstra('a', 'd') == (['a', 'e', 'd'], 4)


def test_real_long():
    """
    Test the longest path having the shortest weight
    """
    g = Graph()
    g.add_node('a')
    g.add_edge('a', 'b', 1)
    g.add_edge('a', 'e', 9000)
    g.add_edge('b', 'c', 1)
    g.add_edge('c', 'e', 1)
    g.add_edge('c', 'd', 6)
    g.add_edge('e', 'd', 3)
    g.add_edge('e', 'f', 1)
    g.add_edge('f', 'd', 1)

    assert g.dijkstra('a', 'd') == (['a', 'b', 'c', 'e', 'f', 'd'], 5)
    assert g.dijkstra('a', 'a') == (['a'], 0)

def test_noeds():
    """
    Test the graph containes correct test_noeds
    """
    g = Graph()
    g.add_node('a')
    g.add_edge('a', 'b', 9)
    g.add_edge('a', 'e', 3)
    g.add_edge('b', 'c', 6)
    g.add_edge('b', 'e', 9000)
    g.add_edge('c', 'd', 6)
    g.add_edge('e', 'c', 5)
    g.add_edge('e', 'd', 1)
    g.add_edge('e', 'f', 3)
    g.add_edge('f', 'a', 8)
    assert 

