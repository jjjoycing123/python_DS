class Node:
    # Constructor of a node
    def __init__(self, data):
        self.data = data
        self.next = None
        self.before = None


class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def peek(self):
        return self.top

    def push(self, node):
        if self.length == 0:
            self.bottom = node
        node.next = self.top
        self.top = node
        self.length = self.length + 1

    def pop(self):
        if self.is_empty == True:
            self.top = None
            self.bottom = None
            return
        temp = self.top
        self.top = temp.next
        self.length = self.length - 1

    def is_empty(self):
        if self.length == 0:
            return True


def stack_print(stack):
    i = 0
    temp = stack
    while temp.next != None:
        print(f"{i} ", temp.data)
        temp = temp.next
        i = i + 1
    print(f"{i} ", temp.data)


if __name__ == '__main__':
    stack = Stack()
    stack.push(Node("Discord"))
    stack.push(Node("Udemy"))
    stack.push(Node("Google"))
    stack.push(Node("Facebook"))
    stack_print(stack.top)
    print("\n")
    stack.pop()
    stack.pop()
    stack_print(stack.top)
    print("\n")
    print("Bottom ", stack.bottom.data)
