class SinglyLinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def calculate_sum(linkedList1, linkedList2):
    constructed_linked_list = SinglyLinkedList(0)
    current = constructed_linked_list
    carry = 0

    while linkedList1 is not None or linkedList2 is not None or carry != 0:
        value_one = linkedList1.value if linkedList1 is not None else 0
        value_two = linkedList2.value if linkedList2 is not None else 0

        sum_of_values = value_one + value_two + carry
        set_new_node(current, sum_of_values)
        current = current.next
        carry = sum_of_values // 10

        linkedList1 = linkedList1.next if linkedList1 is not None else None
        linkedList2 = linkedList2.next if linkedList2 is not None else None

    return constructed_linked_list.next


def set_new_node(current, sum_of_values):
    node_value = sum_of_values % 10
    new_node = SinglyLinkedList(node_value)
    current.next = new_node
