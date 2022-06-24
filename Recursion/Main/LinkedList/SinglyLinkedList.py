class SinglyLinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return 'SinglyLinkedList(value=' + str(self.value) + ' ,next=' + self.next + ')'
