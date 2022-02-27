class Node:
    # Constructor of a node
    def __init__(self, data):
        self.data = data
        self.next = None
        self.before = None


class LinkedList:
    def __init__(self, node):
        self.head = node
        self.tail = self.head
        self.size = 0

    def append(self, node):
        temp = self.tail
        if temp.next != None:
            while temp.next != None:
                temp = temp.next
        temp.next = node
        self.tail = node
        node.before = temp
        self.size = self.size + 1

    def prepend(self, node):
        oldHeadNode = self.head
        node.next = oldHeadNode
        oldHeadNode.before = node
        self.head = node
        self.size = self.size + 1

    def insert(self, node, index):
        if (index >= 0) and (index <= self.size):
            temp_node = self.traverseToIndex(index)
            temp_rest_of_list = temp_node.next
            temp_node.next = node
            temp_node.next.next = temp_rest_of_list
            temp_rest_of_list.before = temp_node.next.next
            self.size = self.size + 1

    def remove(self, index):
        if (index >= 0) and (index <= self.size):
            temp = self.traverseToIndex(index)
            remove_n = temp.next
            temp.next = remove_n.next
            remove_n.next.before = temp.next
            del remove_n
            self.size = self.size - 1

    def traverseToIndex(self, index):
        i = 0
        temp = self.head
        while i < index - 1:
            temp = temp.next
            i = i + 1
        return temp

    def reverseLinkedList(self):
        current_node = self.head
        new_list = None
        if current_node.next != None:
            new_list = Node(current_node.data)
            while current_node.next != None:
                current_node = current_node.next
                temp = Node(current_node.data)
                temp.next = new_list
                new_list = temp
        self.head = new_list


def linkedListPrint(llist):
    i = 0
    temp = llist
    while temp.next != None:
        print(f"{i} ", temp.data)
        temp = temp.next
        i = i + 1
    print(f"{i} ", temp.data)


if __name__ == '__main__':
    llist = LinkedList(Node(1))
    llist.append(Node(4))
    llist.append(Node(5))
    llist.append(Node(6))
    llist.append(Node(9))
    llist.prepend(Node(69))
    llist.prepend(Node(72))
    linkedListPrint(llist.head)
    print("\n")
    llist.insert(Node(78), 2)
    llist.insert(Node(788), 2)
    linkedListPrint(llist.head)
    print("\n")
    llist.remove(2)
    linkedListPrint(llist.head)
    llist.reverseLinkedList()
    print("\n")
    linkedListPrint(llist.head)
    print("\n")
