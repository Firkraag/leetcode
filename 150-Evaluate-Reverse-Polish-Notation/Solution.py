class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for i in tokens:
            
            if isinstance(i, unicode):
                
                if i == '+':
                    stack.append(stack.pop() + stack.pop())
                elif i == '*':
                    stack.append(stack.pop() * stack.pop())
                elif i == '-':
                    op = stack.pop()
                    stack.append(stack.pop() - op)
                elif i == '/':
                    op2 = stack.pop()
                    op1 = stack.pop()
                    stack.append(divide(op1, op2))
                else:
                    stack.append(int(i))
                
            else:
                stack.append(self.evalRPN(i))
        return stack.pop()

def divide(op1, op2):
    if op1 * op2 < 0:
        return (-1 * op1) / op2 * (-1)
    else:
        return op1 / op2
