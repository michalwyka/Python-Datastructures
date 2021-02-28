import unittest
from python_datastructures import SinglyLinkedList


class Test_Queue(unittest.TestCase):
    def setUp(self):
        self.linkedlist = SinglyLinkedList()

    def test_add(self):
        self.linkedlist.add(2)
        self.assertEqual(self.linkedlist.size, 1)
        self.assertEqual(self.linkedlist.head_value, 2)

    
    def test_remove(self):
        self.linkedlist = SinglyLinkedList.from_array([1,3,4,4,3,5,6])
        self.linkedlist.remove_first()
        self.linkedlist.remove_value_from_list([3,6])
        self.linkedlist.remove_value(4, all_occurances=True)
        self.assertEqual(self.linkedlist.array.__str__(), str([3,5]))
    

    def test_empty(self):
        self.assertEqual(self.linkedlist.is_empty, True)
        self.linkedlist.add(3)
        self.assertEqual(self.linkedlist.is_empty, False)

    def test_size(self):
        self.assertEqual(self.linkedlist.size, 0)
        self.linkedlist.add(3)
        self.assertEqual(self.linkedlist.size, 1)

    def test_head_value(self):
        self.assertEqual(self.linkedlist.head_value, None)
        self.linkedlist.add(4)
        self.assertEqual(self.linkedlist.head_value, 4)

    def test_array(self):
        self.linkedlist.add(3)
        self.linkedlist.add(4)
        self.assertEqual(self.linkedlist.array.__str__(), "[4, 3]")


if __name__ == "__main__":
    unittest.main()
