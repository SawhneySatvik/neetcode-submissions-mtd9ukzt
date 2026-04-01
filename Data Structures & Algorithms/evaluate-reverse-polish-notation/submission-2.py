class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            print(stack)
            if token in '+-/*':
                b = stack.pop()
                a = stack.pop()
                c = 0
                if token == '+':
                    c = a + b
                elif token == '-':
                    c = a - b
                elif token == '*':
                    c = a * b
                elif token == '/':
                    c = int(a / b)
                else:
                    break
                stack.append(c)
                print(c)
            else:
                stack.append(int(token))
        return stack.pop()