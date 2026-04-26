class MinStack:

    def __init__(self):
        self.min_stack = []
        self.curr_min = float('+inf')
        

    def push(self, val: int) -> None:
        self.curr_min = min(val, self.curr_min)
        self.min_stack.append(val)

        

    def pop(self) -> None:
        self.min_stack.pop()
        if self.min_stack:
            self.curr_min = min(self.min_stack)
        else:
            self.curr_min = float('inf')
        

    def top(self) -> int:
        return self.min_stack[-1]

    def getMin(self) -> int:
        return self.curr_min
