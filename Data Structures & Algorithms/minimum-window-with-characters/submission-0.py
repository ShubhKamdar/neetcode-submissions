class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or len(t) > len(s):
            return ""

        count = {}
        window = {}

        for char in t:
            count[char] = count.get(char, 0) + 1

        have = 0
        need = len(count)

        left = 0
        minLength = float("inf")
        start = 0

        for right in range(len(s)):

            char = s[right]
            window[char] = window.get(char, 0) + 1

            if char in count and window[char] == count[char]:
                have += 1

            while have == need:

                if right - left + 1 < minLength:
                    minLength = right - left + 1
                    start = left

                window[s[left]] -= 1

                if s[left] in count and window[s[left]] < count[s[left]]:
                    have -= 1

                left += 1

        if minLength == float("inf"):
            return ""

        return s[start:start + minLength]