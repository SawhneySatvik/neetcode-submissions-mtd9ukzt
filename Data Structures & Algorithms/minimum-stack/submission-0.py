class MinStack:

    def __init__(self):
        self.stack = []
        self.min_ele = None

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_ele is None or val < self.min_ele:
            self.min_ele = val

    def pop(self) -> None:
        self.stack.pop()
        self.min_ele = min(self.stack) if self.stack else None

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_ele
