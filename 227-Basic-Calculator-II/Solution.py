class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        operands = []
        operators = []
        s1 = set('+-*/')
        d = dict()
        d['+'] = int.__add__
        d['*'] = int.__mul__
        d['-'] = int.__sub__
        d['/'] = int.__div__
        i = 0
        while i < n:
            if s[i] in s1:
                operators.append(s[i])
                i += 1
            elif s[i] == ' ':
                i += 1
            else:
                start = i   
                while i < n and s[i].isdigit():
                    i += 1
                operands.append(int(s[start:i]))
        result = operands[0]
        i = 0
        n = len(operators)
        while i < n:
            operator = operators[i]
            if i < n - 1 and self.priority(operator, operators[i + 1]):
                value = operands[i + 1]
                i += 1
                while i < n and self.priority(operator, operators[i]):
                    value = d[operators[i]](value, operands[i + 1])
                    i += 1
                result = d[operator](result, value)
            else:
                result = d[operator](result, operands[i + 1])
                i += 1
        return result
        
    def priority(self, operator1, operator2):
        return (operator1 == '+' or operator1 == '-') and (operator2 == '*' or operator2 == '/')
