class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = {}
        window = {}
        left = 0
        right = 0
        k = len(s1)

        if len(s1) > len(s2):
            return False

        for i in s1:
            count[i] = count.get(i, 0) + 1

        while right < len(s2):

            window[s2[right]] = window.get(s2[right], 0) + 1

            if right - left + 1 == k:

                if window == count:
                    return True

                window[s2[left]] -= 1

                if window[s2[left]] == 0:
                    del window[s2[left]]

                left += 1

            right += 1

        return False