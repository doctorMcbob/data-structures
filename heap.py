class BinaryHeap:
    """Binary Heap Data Structure"""
    def __init__(self, iterable=None):
        """Constructor: can be built off an iterable"""
        self.heapList = []
        if iterable is not None:
            for i in iterable:
                self.push(i)

    def restructure(self):
        """restructures up the data tree"""
        i = len(self.heapList) - 1
        while i // 2 > 0:
            if self.heapList[i - 1] < self.heapList[(i // 2) - 1]:
                self.heapList[i - 1], self.heapList[(i // 2) - 1] = (
                    self.heapList[(i // 2) - 1], self.heapList[i])
            i = i // 2

    def restructure2(self):
        """restructures down the data tree"""
        i = 1
        while True:
            try:
                lchild, rchild = i * 2, (i * 2) + 1
                # if left child is more then parent --and--
                # left child is more then or equal to right child
                if (self.heapList[lchild - 1] < self.heapList[i - 1] and
                        self.heapList[lchild - 1] <=
                        self.heapList[rchild - 1]):
                    self.heapList[i - 1], self.heapList[lchild - 1] = (
                        self.heapList[lchild - 1], self.heapList[i - 1])
                    i = i * 2
                # if right child is more then parent --and--
                # right child is more then to left child
                elif (self.heapList[rchild - 1] < self.heapList[i - 1] and
                        self.heapList[rchild - 1] < self.heapList[lchild - 1]):
                    self.heapList[i - 1], self.heapList[lchild - 1] = (
                        self.heapList[lchild - 1], self.heapList[i - 1])
                    i = (i * 2) + 1
                # neither are more then parent
                else:
                    break
            except IndexError:
                break

    def push(self, k):
        """puts number k on the data tree and then restructures"""
        self.heapList.append(k)
        self.restructure()

    def pop(self):
        """removes and returns top of data tree and restructures"""
        item = self.heapList[0]
        self.heapList[0] = self.heapList.pop()
        self.restructure2()
        return item
