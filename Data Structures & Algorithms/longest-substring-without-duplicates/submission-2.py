class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        subs = 0
        seen = set()

        n = len(s)

        while right < n:

            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])

            subs = max(subs, len(seen))

            right += 1

        return subs



        