class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        left_pointer = 0
        maxf = 0
        for index in range(len(s)):
            count[s[index]] = 1 + count.get(s[index], 0)
            maxf = max(maxf, count[s[index]])

            if (index - left_pointer + 1) - maxf > k:
                count[s[left_pointer]] -= 1
                left_pointer += 1
            res  = max(maxf, index - left_pointer + 1)
        return res
