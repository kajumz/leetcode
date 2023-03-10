#using stack and operate with index with this stack

def dailyTemperatures(self, T: List[int]) -> List[int]:
        res = [0]*len(T)
        stack = []
        for i, t in enumerate(T):
            while stack and T[stack[-1]] < t:
                cur = stack.pop()
                res[cur] = i-cur

            stack.append(i)
        return res
