"""Linked list is a linear collection of data elements whose order is not given by their physical placement in memory. Instead, each element points to the next. It is a data structure consisting of a collection of nodes which together represent a sequence. """

from typing import TypeVar


T = TypeVar("T")


class Node:
    def __init__(self, value: T, next=None):
        self.value = value
        self.next = next

    @classmethod
    def from_array(cls, arr):

        """ Function creates linked list from nodes and return head node - use when you want to manipulate in your own functions.
        
        """

        if(len(arr) == 0):
            return cls(None, None)
        else:
            head_node = cls(arr[0])
            current_node = head_node
            for el in arr[1:]:
                current_node.next = Node(el)
                current_node = current_node.next
            return head_node

    def __repr__(self):
        return "Node({}) value type: {} in {}".format(self.value, type(self.value), __name__)
    
    def __str__(self):
        return str(self.value)


class SinglyLinkedList:
    def __init__(self):
        self._sentinel = None          #it's safer in my opinions in case someone type add(None) for
        self._head = self._sentinel
        self._size = 0

    @classmethod
    def from_array(cls, arr):
        ll = cls()
        
        if(len(arr) != 0):
            current_node = Node(arr[0])
            ll._head = current_node
            for el in arr[1:]:
                current_node.next = Node(el)
                current_node = current_node.next
            current_node.next = None
            ll._size = len(arr)

        return ll

    def add(self, value: T) -> None:

        """Add element to linked list at the beginning"""

        self.add_front(value)
    
    def add_front(self, value: T) -> None:

        """Add element to linked list at the begining of list."""

        newNode = Node(value)
        if self._size == 0:
            newNode.next = self._sentinel
            self._head = newNode
        else:
            newNode.next = self._head
            self._head = newNode
            
        self._size += 1

    def add_back(self, value: T) -> None: # I'm not sure this is good adding this function for singlylinked listy

        """Add element to linked list at the end of list."""

        newNode = Node(value)
        newNode.next = self._sentinel
        if self._size == 0:  
            self._head = newNode
        else:
            current_node = self._head
            while not current_node.next is None:
                current_node = current_node.next
            current_node.next = newNode
        
        self._size += 1

    def remove(self):
        return self.remove_first()

    def remove_first(self):

        """ Remove first element from list """

        if self._size == 0:
            return
        else:
            node_to_remove = self._head
            self._head = self._head.next
            self._size -= 1
            return node_to_remove.value
    
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
                    current_node = prev_node.next
                
                self._size -= 1
            else:
                prev_node = current_node
                current_node = current_node.next

    def __iter__(self):

        """Return iterator through nodes"""

        return self.node_iterator()

    def value_iterator(self):

        """Return iterator through values"""

        current_node = self._head
        while not current_node is None:
            yield current_node.value
            current_node = current_node.next

    def node_iterator(self):

        """Return iterator through nodes"""

        current_node = self._head
        while not current_node is None:
            yield current_node
            current_node = current_node.next

    @property
    def head_node(self) -> Node:        # I don't know if it is necessery

        """Return head node."""

        return self._head

    @property
    def head_value(self) -> T:

        """Return value of head element."""

        return self._head.value

    @head_value.setter
    def head_value(self, value : T):

        """Set value of head element."""

        self._head.value = value

    @property
    def size(self) -> int:

        """Return size of the linkedlist."""

        return self._size

    @property
    def is_empty(self) -> bool:
        """Checks if linkedlist is empty."""

        return True if self._size == 0 else False

    def __bool__(self) -> bool:
        return not self.is_empty

    @property
    def array(self) -> list:

        """Converts linkedlist to list."""

        arr = []
        for el in self.value_iterator():
            arr.append(el)

        return arr

    def __len__(self) -> int:
        return self.size

    def __str__(self) -> str:

        """Return String representation of linkedlist values."""

        return " -> ".join(map(str,self.array))

    def __repr__(self) -> str:
        
        return "SinglyLinkedList() size:{} in {}".format(self._size, __name__)


if __name__ == "__main__":
    pass
