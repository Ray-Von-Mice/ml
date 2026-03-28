class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        if n == 1:
            return [0]
        stack = []
        record = [0] * n
        for index, cur_temp in enumerate(temperatures):
            #compared with the top of the stack, aka the day has not find warmer days 
            while stack and cur_temp > stack[-1][0]:
                stack_temp, stack_indx = stack.pop()
                record[stack_indx] = index - stack_indx
            stack.append((cur_temp,  index))
        
        return record