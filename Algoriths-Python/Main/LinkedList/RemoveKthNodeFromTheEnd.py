from Main.LinkedList import SinglyLinkedList


def remove_kth_node_from_the_end(linkedList: SinglyLinkedList, k):
    first_linked_list = linkedList
    second_linked_list = linkedList
    node_count = 1
    while node_count <= k:
        second_linked_list = second_linked_list.next
        node_count += 1
    if second_linked_list is None:
        linkedList.value = linkedList.next.value
        linkedList.next = linkedList.next.next
        return
    while(second_linked_list.next is not None):
        second_linked_list = second_linked_list.next
        first_linked_list = first_linked_list.next

    first_linked_list.next = first_linked_list.next.next

    return linkedList


