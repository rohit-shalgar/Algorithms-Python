import unittest

import Main.LinkedList.SumOfLinkedList as program


class StartLinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


linkedListClass = StartLinkedList
if hasattr(program, "LinkedList"):
    linkedListClass = program.LinkedList


class LinkedList(linkedListClass):
    def addMany(self, values):
        current = self
        while current.next is not None:
            current = current.next
        for value in values:
            current.next = LinkedList(value)
            current = current.next
        return self

    def getNodesInArray(self):
        nodes = []
        current = self
        while current is not None:
            nodes.append(current.value)
            current = current.next
        return nodes


def getNodesInArray(linkedlist):
    nodes = []
    current = linkedlist
    while current is not None:
        nodes.append(current.value)
        current = current.next
    return nodes

class TestPrograms(unittest.TestCase):
    def test_case_1(self):
        linked_list1 = LinkedList(1).addMany([1, 3])
        linked_list2 = LinkedList(0).addMany([3, 4, 5, 6])
        actual = program.calculate_sum(linked_list1, linked_list2)
        expected = LinkedList(1).addMany([4,7,5,6])

        self.assertEqual(getNodesInArray(actual),getNodesInArray(expected))
