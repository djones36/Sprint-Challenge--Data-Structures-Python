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
    1. append(): add to the head each time the newst item
    ['1', '2', '3']
    ['4', '1', '2', '3']
    ['5', '4', '1', '2', '3']

    Check if memory is full.
    
    2. replace oldest once full
    ['5', '4', '1', '2', '3']
    ['6', '5', '4', '1', '2']
    ['7', '6', '5', '4', '1']

    3. get() to return the list.
'''


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.current is None:
            self.current = 1

        if self.storage.length == self.capacity:
            if self.current is 1:
                self.storage.remove_from_head()
                self.storage.add_to_head(item)
                self.current += 1
            elif self.current is 2:
                self.storage.head.next.insert_after(item)
                self.storage.head.next.delete()
                self.current += 1
            elif self.current is 3:
                self.storage.head.next.next.insert_after(item)
                self.storage.head.next.next.delete()
                self.current += 1
            elif self.current is 4:
                self.storage.tail.prev.insert_before(item)
                self.storage.tail.prev.delete()
                self.current += 1
            elif self.current is 5:
                self.storage.remove_from_tail()
                self.storage.add_to_tail(item)
                self.current = 1
        else:
            self.storage.add_to_tail(item)

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        node = self.storage.head
        while node:
            list_buffer_contents.append(node.value)
            node = node.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
