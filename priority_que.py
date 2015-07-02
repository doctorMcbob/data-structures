class Node(object):
    def __init__(self, val, pointer, priority=0):
        self.value = val
        self.nextNode = pointer
        self.priority = priority

        
class PriorityQueue(object):
    def __init__(self):
        self._size = 0
        self.first = None
        self.last = None

    def restructure(self):
        """
        restructure method: 
          moves the node down the list untill it outranks
          it's nextNode. 
        """
        if self.first.priority >= self.first.nextNode.priority:
            node = self.first
            while node.nextNode.priority >= node.priority:
                prev_node = node.nextNode
                node.nextNode = node.nextNode.nextNode
            prev_node.nextNode = node
        
    def insert(self, val, priority=0):
        """
        insert method:
          adds new value to the front of the list
          and then calls the restructure method
          which makes sure the node is in the right spot
        """
        if self._size == 0:
            self.first = Node(val, None)
            self.last = self.first
        else:
            self.first, self.first.nextNode = Node(val, None. priority), self.first
            self.restructure()
        self._size += 1
        
        
    def pop(self):
        """
        pop method:
           removes the value at the head of the list and returns it
        """
        node = self.first
        self.first = self.first.nextNode
        self._size -= 1
        return node.value

    def size(self):
        return self._size

    def peek(self):
        return self.first
