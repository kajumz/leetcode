#using stack and push with val, curmin

class MinStack:

    def __init__(self):
        self.q = []
        

    def push(self, val: int) -> None:
        curmin = self.getMin()
        if curmin == None or val < curmin:
            curmin = val
        self.q.append((val,curmin))

    def pop(self) -> None:
        self.q.pop()

    def top(self) -> int:
        if len(self.q) == 0:
            return None
        return self.q[len(self.q)-1][0]
        

    def getMin(self) -> int:
        if len(self.q) == 0:
            return None
        return self.q[len(self.q)-1][1]
