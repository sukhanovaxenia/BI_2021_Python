import unittest

import linked_tests



class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.linked_list = linked_tests.LinkedList()

    def test_len(self):
        self.assertEqual(0, self.linked_list.__len__())

    def test_addNoIndex(self):
        current = self.linked_list
        current.add("one")
        self.assertEqual(1, current.__len__())
        self.assertTrue(current.__contains__("one"))

    def test_addByIndex(self):
        current = self.linked_list
        current.extend([1, 2])
        current.add("first", index=0)
        self.assertEqual(3, current.__len__())
        self.assertEqual("first", current.__getitem__(0))
        self.assertEqual(2, current.last())

    def test_extend(self):
        values = ["one", "two", "bang!"]
        current = self.linked_list
        current.extend(values)
        self.assertEqual(3, current.__len__())
        self.assertTrue(current.__contains__("bang!"))
        self.assertFalse(current.__contains__(str(1)))
        self.assertEqual("one", current.first())
        self.assertEqual("two", current.__getitem__(1))
        self.assertEqual("bang!", current.last())

    def test_pop(self):
        current = self.linked_list
        current.extend([1, 2, 3, "out", 4, 5])
        self.assertTrue(current.pop().list_iterator() == [1, 2, 3, "out", 4])
        self.assertTrue(current.pop(index=1).list_iterator() == [1, 3, "out", 4])
        self.assertFalse(current.pop().list_iterator() == [2, 3, 'out', 4])
        self.assertEqual(current.pop().__len__(), 2)

    def test_in(self):
        current = self.linked_list
        current.add("How do you do?")
        self.assertTrue(current.__contains__("do"))
        self.assertFalse(current.__contains__("are"))

    def test_last_occurrence_remove(self):
        current = self.linked_list
        current.extend([6, 5, 4, 3, 8, 6, 6])
        self.assertTrue(current.last() == 6)
        self.assertEqual(current.__len__(), 7)
        self.assertTrue(current.first() == 6)

        

    