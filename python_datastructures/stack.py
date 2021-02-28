"""Stack is an abstract data type that serves as a collection of elements, with two main principal operations: Push, which adds an element to the collection, and Pop, which removes the most recently added element that was not yet removed."""

from python_datastructures.linkedlist import SinglyLinkedList
from typing import TypeVar
import copy


T = TypeVar("T")


class Stack:
    def __init__(self, max_size=None):
        self.__stack = SinglyLinkedList()
        self.__max_size = None

    @classmethod
    def from_array(cls, arr):

        """ Create stack from array. Element at index 0 is at the bottom of stack """

        s = cls()
        s.__stack = SinglyLinkedList.from_array(arr)
        return s

    @classmethod
    def from_linked_list(cls, llist):
        s = cls()
        s.__stack = copy.deepcopy(llist)
        return s

    def push(self, value: T) -> None:

        """Add element to the top of the stack."""

        if self.is_full:
            raise Exception("Stack is full!")

        self.__stack.add(value)

    def pop(self) -> T:

        """Remove element from the top of the stack."""

        return self.__stack.remove()

    def peek(self) -> T:

        """View top element in the stack."""

        return self.__stack.head_value

    @property
    def is_full(self) -> bool:
        if (not self.__max_size is None) and (self.__stack.size == self.__max_size):
            return True
        else:
            return False

    @property
    def is_empty(self) -> bool:

        """Check if stack is empty."""

        return True if self.__stack.size == 0 else False

    def __bool__(self) -> bool:
        return self.is_empty

    @property
    def size(self) -> int:

        """Get size of the stack."""

        return self.__stack.size

    def __repr__(self) -> str:
        return "Stack() size: {}".format(self.__stack.size)

    def __str__(self) -> str:

        """Get string representation of the stack."""

        return "bottom: " + str(self.__stack.array)


if __name__ == "__main__":
    pass
