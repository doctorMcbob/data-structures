class BinaryHeap:
    def __init__(self):
        self.heapList = []

    def restructure(self,i):
        i = len(self.heapList)
        while i // 2 > 0:
          if self.heapList[i] < self.heapList[i // 2]:
             tmp = self.heapList[i // 2]
             self.heapList[i // 2] = self.heapList[i]
             self.heapList[i] = tmp
          i = i // 2

    def push(self,k):
        self.heapList.append(k)
        self.restructure()

    def pop(self):
        item = self.heapList[0]
        self.heapList[0] = self.heapList[-1]
        self.restructure()
        return item


