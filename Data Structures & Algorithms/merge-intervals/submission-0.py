class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda pair: pair[0])

        stack = []
        for curr_s, curr_e in intervals:
            if stack and curr_s <= stack[-1][1]:
                stack_s, stack_e = stack.pop()
                stack.append([min(curr_s, stack_s), max(curr_e, stack_e)])
            else:
                stack.append([curr_s, curr_e])
        
        return stack
        