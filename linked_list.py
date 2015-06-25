class LinkedList(object):
    def __init__(self, iterable=()): #LinkedList((1, 2, 3)) --> (1, 2, 3)
        self.ll = {}
        for node in iterable:
            self.ll[len(self.ll)+1] = node
    
    def insert(self, val): #basically append
        self.ll[len(self.ll)+1]=val
        
    def pop(self): #remove and return end of list
        node = self.ll[len(self.ll)]
        del self.ll[len(self.ll)]
        return node
        
    def size(self): #return length of list
        return len(self.ll)

    def search(self, val): #remove and return node based on index |
                           #return none if node does not exist
        try:
            node = self.ll[val]
            i=val
            while i < len(self.ll):
                self.ll[i] = self.ll[i+1]
                i+=1
            del self.ll[len(self.ll)]
            return node
        except KeyError:
            return None

    def remove(self, node): #remove node without index
        i=1
        while i < len(self.ll):
            if self.ll[i] == node:
                self.search(i)
                break
            i+=1
        
    def display(self): #return tuple literal of list items
        t, i = (), 1
        while i < len(self.ll)+1:
            t = t[:i]+(self.ll[i], )+t[i:]
            print t
            raw_input
            i+=1
        return t
