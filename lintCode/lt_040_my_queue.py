class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, element):
        self.stack1.append(element)

    def top(self):
        self.__move()
        return self.stack2[-1]

    def pop(self):
        self.__move()
        return self.stack2.pop()

    def __move(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
