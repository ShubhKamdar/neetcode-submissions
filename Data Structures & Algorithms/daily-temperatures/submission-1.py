class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        output =[0]*n
        stack = []

        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                previous_day = stack.pop()
                output[previous_day] = i - previous_day

            stack.append(i)
        return output
