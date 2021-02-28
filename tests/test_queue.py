import unittest
from python_datastructures.queue import Queue


class Test_Queue(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()

    def test_enqueue(self):
        self.queue.enqueue(2)
        self.assertEqual(self.queue.size, 1)

    def test_dequeue(self):
        self.queue.enqueue(3)
        self.assertEqual(self.queue.size, 1)
        self.queue.dequeue()
        self.assertEqual(self.queue.size, 0)

    def test_isEmpty(self):
        self.assertEqual(self.queue.is_empty, True)
        self.queue.enqueue(3)
        self.assertEqual(self.queue.is_empty, False)

    def test_getSize(self):
        self.assertEqual(self.queue.size, 0)
        self.queue.enqueue(3)
        self.assertEqual(self.queue.size, 1)

    def test_get_tail(self):
        self.assertEqual(self.queue.tail_value, None)
        self.queue.enqueue(3)
        self.assertEqual(self.queue.tail_value, 3)

    def test_get_head(self):
        self.assertEqual(self.queue.head_value, None)
        self.queue.enqueue(3)
        self.assertEqual(self.queue.head_value, 3)


if __name__ == "__main__":
    unittest.main()
