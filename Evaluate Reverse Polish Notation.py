#use stack and do operations with 2 on top while find operator

def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for t in tokens:
            if t not in "+-/*":
                stack.append(int(t))
            else:
                r,l=stack.pop(),stack.pop()
                if t == "+":
                    stack.append(r+l)
                if t == "-":
                    stack.append(l-r)
                if t == "*":
                    stack.append(l*r)
                if t == "/":
                    stack.append(int(float(l)/r))

        return stack.pop()
