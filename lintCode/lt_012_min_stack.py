class MinStack(object):
    def __init__(self):
        self.f = []
        self.m = []

    def push(self, element):
        self.f.append(element)
        if not self.m or self.m[-1] >= element:
            self.m.append(element)

    def pop(self):
        val = self.f.pop()
        if val == self.m[-1]:
            self.m.pop()
        return val

    def min(self):
        return self.m[-1]
