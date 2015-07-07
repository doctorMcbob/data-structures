class Node(object):
    """Node class. has a value and a list of pointers"""
    def __init__(self, val, pointers=None):
        self.value = val
        self.pointers = []


class SimpleGraph(object):
    """Graph data structure"""
    def __init__(self, nodes=[]):
        self.nodes = nodes

    def nodes(self):
        """Returns a list of nodes"""
        return self.nodes

    def edges(self):
        """Returns a list of all the edges in the graph
        [(n1, n2), (n1, n2), ...] where n1 has a pointer to n2"""
        pass

    def add_node(self, n):
        """Puts a node into the graph"""
        self.nodes.append(n)

    def add_edge(self, n1, n2):
        """Creates an edge between two nodes
        n1 points to n2"""
        if n1 not in self.nodes:
            self.add_node(n1)
        if n2 not in self.nodes:
            self.add_node(n2)
        n1.pointers.append(n2)

    def del_node(self, n):
        """Removes node from the graph"""
        pass

    def del_edge(self, n1, n2):
        """Removes edge from graph
        removes pointer to n2 from n1"""
        n1.pointers.remove(n2)

    def has_node(self, n):
        """Returns True if node n is in the graph
        and False if it is not"""
        if n in self.nodes:
            return True
        else:
            return False

    def neighbors(self, n):
        """Returns a list of all the nodes connected
        to n by edges. Error if n is not in the graph"""
        pass

    def adjacent(self, n1, n2):
        """Returns True if n1 and n2 have an edge.
        Error if either are not in the graph"""
        pass
