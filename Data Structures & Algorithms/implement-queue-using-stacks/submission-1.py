class MyQueue:

    def __init__(self):
        self.stack = []
        self.rev = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        
    def pop(self) -> int:
        self.rev = self.stack[::-1]
        node = self.rev.pop()
        self.stack = self.rev[::-1]
        return node

    def peek(self) -> int:
        self.rev = self.stack[::-1]
        return self.rev[-1]


    def empty(self) -> bool:
        if self.stack:
            return False
        return True
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()