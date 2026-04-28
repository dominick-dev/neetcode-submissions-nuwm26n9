class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for op in operations:
            if op == '+':
                first = stack[-1]
                sec = stack[-2]
                stack.append(first + sec)
            elif op == 'D':
                prev = stack[-1]
                stack.append(prev * 2)
            elif op == 'C':
                stack.pop()
            else:
                stack.append(int(op))
        
        return sum(stack)
        