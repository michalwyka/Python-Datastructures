"""Doubly linked list is a linked data structure that consists of a set of sequentially linked records called nodes. Each node contains three fields: two link fields and one data field."""

from python_datastructures.linkedlist import SinglyLinkedList
from python_datastructures.linkedlist import Node as SLL_Node
from typing import TypeVar


T = TypeVar("T")

"""
class Node:
    def __init__(self, value: T):
        self.value = value
        self.next = None
        self.prev = None
"""

class Node(SLL_Node):
    def __init__(self, value : T, prev=None, next=None):
        super(Node, self).__init__(value, next)
        self.prev = prev

    @classmethod
    def from_array(cls, arr):
        if(len(arr) == 0):
            return cls(None, None, None)
        else:
            head_node = cls(arr[0])
            current_node = head_node
            prev_node = None
            for el in arr[1:]:
                current_node.next = Node(el)
                current_node.prev = prev_node

                prev_node = current_node
                current_node = current_node.next
                
            return head_node


class DoublyLinkedList(SinglyLinkedList):
    def __init__(self):
        super(DoublyLinkedList, self).__init__()
        self._tail = self._sentinel

    @classmethod
    def from_array(cls, arr):
        dl = cls()

        if(len(arr) != 0):
            current_node = Node(arr[0], None, None)
            dl._head = current_node

            for el in arr[1:]:
                current_node.next = Node(el, current_node, None)
                current_node = current_node.next
            current_node.next = None
            dl._tail = current_node
            print(dl._tail.prev)
            dl._size = len(arr)
        
        return dl

    def add_front(self, value: T) -> None:
        if self.size == 0:
            self._head = Node(value, None, None)
            self._tail = self._head
        else:
            newNode = Node(value, None, self._head)
            self._head.prev = newNode
            self._head = newNode

    def add_back(self, value: T) -> None:
        if self._size == 0:
            newNode = Node(value, self._sentinel, self._sentinel)
            self._head = newNode
            self._tail = newNode
        else:
            newNode = Node(value, self._tail, self._sentinel)
            self._tail = newNode
        self._size += 1

    def remove_first(self):
        if self.size == 0:
            return
        else:
            ret = super(DoublyLinkedList, self).remove_first()
            self._head.prev = None
            return ret

    def remove_last(self):
        if self.size == 0:
            return
        else:
            ret = self._tail.value
            self._tail = self._tail.prev
            self._tail.next = None
            return ret

    def remove_value(self, value: T, all_occurances=False):

        """ Remove element which value is equal to value argument.
            If all_occurances = False - remove first occureance
            else remove all occurances in list
        """

        while self._head.value == value:
                self.remove_first()
                if all_occurances is False:
                    return
        
        prev_node = self._head
        current_node = self._head.next
        while not current_node.next is None:
            if current_node.value == value:
                prev_node.next = current_node.next
                current_node.next.prev = prev_node
                current_node = prev_node.next
                self._size -= 1
                if all_occurances is False:
                    return
            else:
                prev_node = current_node
                current_node = current_node.next

    def remove_value_from_list(self, values: list, all_occurances=False):

        """ Remove elements which belongs to list values. If all_occurances is False removes
            only first occurance of element """

        prev_node = None
        current_node = self._head

        while not current_node is None:
            if current_node.value in values:
                if all_occurances is False:
                    values.remove(current_node.value)

                if prev_node is None:
                    self._head = self._head.next
                    current_node = self._head
                else:
                    prev_node.next = current_node.next
                    current_node.next.prev = prev_node
                    current_node = prev_node.next
                
                self._size -= 1
            else:
                prev_node = current_node
                current_node = current_node.next

    def addAtHead(self, value: T) -> None:  # compability

        """Add node at head end."""

        self.add_front(value) 

    def addAtTail(self, value: T) -> None: # compability

        """Add node at tail end."""

        self.add_back(value)

    def removeAtHead(self):

        """Remove node at head end."""

        self.remove_first()

    def removeAtTail(self):

        """Remove node at tail end."""

        pass

    def reversed_value_iterator(self):

        """Return iterator through values in reverse"""

        current_node = self._tail
        while not current_node is None:
            yield current_node.value
            current_node = current_node.prev

    def reversed_node_iterator(self):

        """Return iterator through nodes in reverse"""

        current_node = self._tail
        while not current_node is None:
            yield current_node
            current_node = current_node.prev
    
    def __reversed__(self):
        
        return self.reversed_node_iterator()

    @property
    def tail_value(self) -> T:

        """Get value at the tail of the list."""

        return self._tail.value

    @tail_value.setter
    def tail_value(self, value: T):


        """Set value of head element."""

        self._tail.value = value

    def __str__(self) -> str:

        """Return String representation of linkedlist values."""

        return " <-> ".join(map(str,self.array))

    def __repr__(self) -> str:
        
        return "DoublyLinkedList() size:{} in {}".format(self._size, __name__)


if __name__ == "__main__":
    pass
