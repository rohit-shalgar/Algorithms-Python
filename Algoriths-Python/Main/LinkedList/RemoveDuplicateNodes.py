from Main.LinkedList import SinglyLinkedList


def remove_duplicate_nodes(linkedList: SinglyLinkedList):
    current_linked_list = linkedList

    while current_linked_list is not None:
        next_node = current_linked_list.next

        while next_node is not None and next_node.value == current_linked_list.value:
            next_node = next_node.next
        current_linked_list.next = next_node
        current_linked_list = current_linked_list.next

    return linkedList

