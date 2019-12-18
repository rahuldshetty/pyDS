class Stack:

    def __init__(self):
        self.__stack = []
        self.__top = -1

    def push(self, element):
        self.__top += 1
        self.__stack.append(element)

    def top(self):
        if self.__top == -1:
            raise Exception("Stack Empty!")
        else:
            return self.__stack[self.__top]

    def pop(self):
        if self.__top == -1:
            raise Exception("Stack Underflow Exception!")
        else:
            element = self.top()
            del self.__stack[self.__top]
            self.__top -= 1
            return element

    def length(self):
        return self.__top + 1

    def print_(self):
        print(self.__stack)


if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    print(stack.top())
    print(stack.pop())
    print(stack.length())
    print(stack.pop())
    print(stack.length())
