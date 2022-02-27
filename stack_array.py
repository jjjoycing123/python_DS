class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0
        self.array = []

    def peek(self):
        return self.top

    def push(self, value):
        if self.length == 0:
            self.bottom = value
        self.array.append(value)
        self.length = self.length + 1
        self.top = self.array[self.length - 1]

    def pop(self):
        if self.is_empty == True:
            self.top = None
            self.bottom = None
            return
        self.array.pop()
        self.length = self.length - 1

    def is_empty(self):
        if self.length == 0:
            return True


def stack_print(stack):
    i = 0
    for value in reversed(stack):
        print(f"{i} ", value)
        i = i + 1


if __name__ == '__main__':
    stack = Stack()
    stack.push("Discord")
    stack.push("Udemy")
    stack.push("Google")
    stack.push("Facebook")
    stack_print(stack.array)
    print("\n")
    print(stack.length)
    print(stack.top)
    print(stack.bottom)
    print("\n")
    stack.pop()
    stack.pop()
    stack_print(stack.array)