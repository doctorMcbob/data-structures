class BinaryHeap:
    """Binary Heap Data Structure"""
    def __init__(self, iterable=None):
        """Constructor: can be built off an iterable"""
        self.heapList = [None]
        if iterable is not None:
            for i in iterable:
                self.push(i)

    def restructure(self):
        """restructures up the data tree"""
        i = len(self.heapList) - 1
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                self.heapList[i], self.heapList[i//2] = self.heapList[i//2], self.heapList[i]
            i = i // 2

    def restructure2(self):
        """restructures down the data tree"""
        i = 1
        while True:
            try:
                if self.heapList[i * 2] > self.heapList[(i * 2) + 1]:
                    self.heapList[i], self.heapList[(i * 2) + 1] = self.heapList[(i * 2) + 1], self.heapList[i]
                    i = (i * 2) + 1
                elif self.heapList[i * 2] < self.heapList[(i * 2) + 1]:
                    self.heapList[i], self.heapList[i * 2] = self.heapList[i*2], self.heapList[i]
                    i = i * 2
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
        item = self.heapList[1]
        self.heapList[1] = self.heapList.pop()
        self.restructure2()
        return item