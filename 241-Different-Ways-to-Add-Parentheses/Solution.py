class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        n = len(input)
        s = set(['-', '+', '*'])
        operands = []
        operators = []
        start = 0
        # construct operands list and operators list
        for i in range(n):
            if input[i] in s:
                operands.append(int(input[start:i]))
                operators.append(input[i])
                start = i + 1
        operands.append(int(input[start:n]))
        if len(operands) == 1:
            return operands
        result = []
        n = len(operands)
        for i in range(n):
            result.append([])
            l = result[-1]
            for j in range(n):
                l.append([])
        print operands, operators
        self.diffWaysToComputeAux(operators, operands , 0, len(operands) - 1, result)
        return result[0][n - 1]
        
    def diffWaysToComputeAux(self, operators, operands, start, end, result):
        if start == end:
            result[start][end].append(operands[start])
            return
        for i in range(start, end):
            if len(result[start][i]) == 0:
                self.diffWaysToComputeAux(operators, operands, start, i, result)
            if len(result[i + 1][end]) == 0:
                self.diffWaysToComputeAux(operators, operands, i + 1, end, result)
            valList1 = result[start][i]
            valList2 = result[i + 1][end]
            if operators[i] == '+':
                for val1 in valList1:
                    for val2 in valList2:
                        result[start][end].append(val1 + val2)
            elif operators[i] == '*':
                for val1 in valList1:
                    for val2 in valList2:
                        result[start][end].append(val1 * val2)
            if operators[i] == '-':
                for val1 in valList1:
                    for val2 in valList2:
                        result[start][end].append(val1 - val2)
            
