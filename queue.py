class Node:
    def __init__(self, data):
        self.next = None
        self.before = None
        self.data = data


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def peek(self):
        return self.first

    def enqueue(self, Node):
        if self.length == 0:
            self.first = Node
            self.last = Node
            self.length = self.length + 1
            return
        old_last = self.last
        Node.next = old_last
        old_last.before = Node
        self.last = Node
        self.length = self.length + 1

    def dequeue(self):
        if self.length >= 1:
            new_first = self.first.before
            self.first = new_first
            self.first.next = None
            self.length = self.length - 1

    def is_empty(self):
        if self.length > 0:
            return True


def queue_print(queue):
    i = 0
    temp = queue
    while temp.next != None:
        print(f"{i} ", temp.data)
        temp = temp.next
        i = i + 1
    print(f"{i} ", temp.data)


if __name__ == '__main__':
    queue = Queue()
    queue.enqueue(Node("Joy"))
    queue.enqueue(Node("Matt"))
    queue.enqueue(Node("Pavel"))
    queue.enqueue(Node("Samir"))
    queue_print(queue.last)
    print("\n")
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue_print(queue.last)
