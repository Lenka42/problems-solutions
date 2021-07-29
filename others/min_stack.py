class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.q = []

    def push(self, val: int) -> None:
        if self.q:
            curr_min = min(val, self.q[-1][1])
            self.q.append((val, curr_min))
        else:
            self.q.append((val, val))

    def pop(self) -> None:
        val, _ = self.q.pop()
        return val

    def top(self) -> int:
        return self.q[-1][0]

    def getMin(self) -> int:
        return self.q[-1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()