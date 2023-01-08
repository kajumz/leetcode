# using stack
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapps = {')':'(',
                 '}':'{',
                 ']':'['}
        for char in s:
            if char in mapps:
                if len(stack) != 0:
                    top_element = stack.pop()
                else:
                    top_element = '#'
                if mapps[char] != top_element:
                    return False

            else:
                stack.append(char)
        return not stack
