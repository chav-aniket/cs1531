class Stack:
    def __init__(self):
        self.__stack = []

    def push(self, x):
        self.__stack.append(x)

    def pop(self):
        return self.__stack.pop()

def test_stack():
    stack = Stack()
    stack.push("Hello")
    stack.push("How are you?")
    stack.push("Goodbye")

    assert stack.pop() == "Goodbye"
    assert stack.pop() == "How are you?"
    assert stack.pop() == "Hello"
