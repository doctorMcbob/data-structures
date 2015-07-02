from heap import BinaryHeap


def test_push():
    heap = BinaryHeap((1, 3, 8, 26, 4, 15, 20, 88, 23, 7, 11, 40))
    print heap.heapList
    assert heap.heapList[0] == 1
    assert heap.heapList[3] == 7
    # assert heap.heapList[3] == 6


def test_pop():
    heap = BinaryHeap((1, 3, 8, 26, 4, 15, 20, 88, 23, 7, 11, 40))
    heap.pop()
    assert heap.heapList[0] == 3
    assert heap.heapList[-2] == 7
    heap.pop()
