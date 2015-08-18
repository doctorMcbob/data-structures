# -*- coding: utf-8 -*-
from __future__ import unicode_literals


class Node(object):
    """Node class. has a value and a list of pointers"""
    def __init__(self, val=None, iterable=[]):
        self.value = val
        self.pointers = []
        for pointer in iterable:
            self.pointers.append(pointer)

    def get_edges(self):
        return self.pointers


class Edge(object):
    def __init__(self, n1, n2, weight=0):
        self.n1 = n1
        self.n2 = n2
        self.weight = weight


class WeightedGraph(object):
    """Weighted Graph data structure"""
    def __init__(self, iterable=[]):
        self._nodes = []
        for node in iterable:
            self.add_node(node)

    def nodes(self):
        """Returns a list of nodes"""
        return self._nodes

    def edges(self):
        """Returns a list of all the edges in the graph
        [(n1, n2), (n1, n2), ...] where n1 has a pointer to n2"""
        l = []
        for n in self.nodes():
            for edge in n.pointers:
                l.append((n, edge.n2, edge.weight))
        return l

    def add_node(self, n):
        """Puts a node into the graph"""
        self._nodes.append(n)

    def add_edge(self, n1, n2, weight=0):
        """Creates an edge between two nodes
        n1 points to n2"""
        if n1 not in self.nodes():
            self.add_node(n1)
        if n2 not in self.nodes():
            self.add_node(n2)
        if n2 not in n1.pointers:
            n1.pointers.append(Edge(n1, n2, weight))

    def del_node(self, n):
        """Removes node from the graph"""
        if not self.has_node(n):
            raise ValueError("Node is not in the graph")
        for node in self.nodes():
            if self.adjacent(node, n):
                self.del_edge(node, n)
        self._nodes.remove(n)

    def del_edge(self, n1, n2):
        """Removes edge from graph
        removes pointer to n2 from n1"""
        if not (self.has_node(n1) and self.has_node(n2)):
            raise ValueError("Node is not in the graph")
        for edge in n1.pointers:
            if edge.n2 == n2:
                n1.pointers.remove(edge)
                break

    def has_node(self, n):
        """Returns True if node n is in the graph
        and False if it is not"""
        return n in self.nodes()

    def neighbors(self, n):
        """Returns a list of all the nodes connected
        to n by edges. Error if n is not in the graph"""
        if not self.has_node(n):
            raise ValueError("Node is not in the graph")
        return [e.n2 for e in n.pointers]

    def adjacent(self, n1, n2):
        """Returns True if n1 and n2 have an edge.
        Error if either are not in the graph"""
        if not (self.has_node(n1) and self.has_node(n2)):
            raise ValueError("Node is not in the graph")
        for edge in n1.pointers:
            if edge.n2 == n2:
                return True
        else:
            return False

    def depth_first_traversal(self, start):
        """Returns a depth first traversal path as a list.
        """
        visited = []
        begin = [start]

        while begin:
            node = begin.pop(0)
            if node not in visited:
                visited.append(node)
                begin = self.neighbors(node) + begin
        return visited

    def breadth_first_traversal(self, start):
        """Returns a breadth first travesal path as a list.
        """
        visited = []
        begin = [start]

        while begin:
            node = begin.pop(0)
            if node not in visited:
                visited.append(node)
                begin = begin + self.neighbors(node)
        return visited

    def traverse_path(self, start, end):
        path = ([], 0)
        paths = []
        node = start
        while True:
            edges = node.get_edges()
            for edge in edges:
                paths.append((path[0] + [edge], path[1] + edge.weight))
