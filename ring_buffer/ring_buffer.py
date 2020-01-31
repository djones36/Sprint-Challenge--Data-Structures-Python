from doubly_linked_list import DoublyLinkedList
'''
    Similar to LRU_cache
    When a new item is added to the (head), the oldest item(tail) is overwritten if the cache is full. 
    Methods available: get() and append()
        get(): Returns a list of all of th item in the cache.
        append(): adds item to the head of the list.
    May not use python list on the append()
    May not return None values in the list(need a null check)

    Plan:
    1. append(): add to the tail each time the newst item
    ['a', 'b', 'c']
    ['a', 'b', 'c', 'd']
    ['a', 'b', 'c', 'd', 'e']

    Check if memory is full.
    
    2. replace oldest once full
    ['a', 'b', 'c', 'd', 'e']
    ['a', 'b', 'c', 'd', 'w']
    ['a', 'b', 'c', 'd', 'z']

    3. get() to return the list.
'''


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        pass

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
