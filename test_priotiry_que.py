from priority_que import PriorityQueue
import pytest


#@pytest.fixture
def makeapq():
    pq = PriorityQueue()
    pq.insert("duck", 2)
    pq.insert(3, 1)
    pq.insert("fish", 5)
    pq.insert("money", 5)
    pq.insert(4, 2)
    return pq


def test_insert():
    pq = makeapq()
    assert pq.first.value == "fish"
    

def test_pop():
    pq = makeapq()
    assert ["fish", "money", "duck", 4, 3] == [pq.pop() for x in range(5)]
    
