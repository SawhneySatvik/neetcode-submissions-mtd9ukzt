class Solution:
    def isValid(self, s: str) -> bool:
        paren = {
            '}':'{',
            ']':'[',
            ')':'('
        }

        stack = []

        for p in s:
            if p in '([{':
                stack.append(p)
            else:
                if stack and stack[-1] == paren[p]:
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0