"""In computer science, a queue is a collection of entities that are maintained in a sequence and can be modified by the addition of entities at one end of the sequence and the removal of entities from the other end of the sequence."""

from python_datastructures.doublylinkedlist import DoublyLinkedList
from typing import TypeVar


T = TypeVar("T")


class Node:
    def __init__(self, value: T):
        self.value = value
        self.next = None
        self.previous = None


class Queue:
    def __init__(self):
        self._queue = DoublyLinkedList()

    @classmethod
    def from_array(cls, arr):
        q = cls()
        q._queue = DoublyLinkedList.from_array(arr)
        return q

    @property
    def head_value(self) -> T:

        """View first element in the queue."""

        return self._queue.head_value

    @property
    def tail_value(self):

        """View last element in the queue."""

        return self._queue.tail_value

    def dequeue(self) -> T:

        """Remove element from the queue."""

        return self._queue.remove_first()

    def enqueue(self, value: T) -> None:

        """Add element to queue."""

        self._queue.add_back(value)

    @property
    def array(self) -> list:
        return self._queue.array

    @property
    def size(self) -> int:

        """Get size of the queue."""

        return self._queue.size

    @property
    def is_empty(self) -> bool:

        """Check if queue is empty."""

        return self._queue.is_empty

    def __bool__(self) -> bool:
        return not self.is_empty

    def __len__(self) -> int:
        return self.size

    def __repr__(self) -> str:
        return "Queue() size:{} in {}".format(self.size, __name__)

    def __str__(self) -> str:

        """Get string representation of the queue."""

        return self._queue.__str__()


if __name__ == "__main__":
    pass
