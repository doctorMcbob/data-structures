from linked_list import LinkedList
import pytest 

def test_constructor():
    items=("duck", 3, [2, 3, 4], object())
    ll=LinkedList(items)
    ll2=LinkedList()
    for i in items:
        ll2.insert(i)
    for i in items:
        assert ll.pop() == ll2.pop()


def test_insert():
    ll = LinkedList()
    ll.insert(5)
    assert ll.ll[1] == 5

        
def test_pop():
    LL = LinkedList(("dog", 3, "fish taco", object(), "house"))
    assert  "house" == LL.pop()
    
def test_size():
    LL = LinkedList(("dog", 3, "fish taco", object(), "house"))
    assert len(LL.ll) == 5

def test_search():
    LL = LinkedList(("dog", 3, "fish taco", object(), "house"))
    assert LL.search(2) == 3
    assert LL.search(10) == None
    
def test_remove():
    LL = LinkedList(("dog", 3, "fish taco", object(), "house"))
    LL.remove("fish taco")
    assert len(LL.ll) == 4

def test_display():
    items=("duck", 3, [2, 3, 4], object())
    ll=LinkedList(items)
    assert items == ll.display()

