import pytest

def test_constructor():
    items=("duck", 3, [2, 3, 4], object())
    ll=LinkedList(items)
    ll2=LinkedList()
    for i in items:
        ll2.insert(i)
    for i in items:
        assert ll.pop() == ll2.pop()

def test_display():
    items=("duck", 3, [2, 3, 4], object())
    ll=LinkedList(items)
    assert items == ll.display()
    
from linked_list import LinkedList
