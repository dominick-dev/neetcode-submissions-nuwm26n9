class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        res = 0

        for op in operations:
            if op == '+':
                first = stack[-1]
                sec = stack[-2]
                res += (first + sec)
                stack.append(first + sec)
            elif op == 'D':
                prev = stack[-1]
                res += (prev * 2)
                stack.append(prev * 2)
            elif op == 'C':
                res -= stack[-1]
                stack.pop()
            else:
                res += int(op)
                stack.append(int(op))
        
        return res
        