class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        maps = {
            ']':'[',
            ')':'(',
            '}':'{'
        }

        for char in s:
            if char in maps:
                if not stack or stack[-1] != maps[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)
        return len(stack) == 0







