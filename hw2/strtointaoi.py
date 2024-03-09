class Solution:
    def myAtoi(self, s: str) -> int:
        nums = '0123456789'
        symbols = '-'
        res_str = ''
        can_zero = False
        if s[0] not in nums and s[0] not in symbols and s[0] != ' ':
                return 0
        for c in s:
            if c == '0' and can_zero:
                res_str += c
            if c in nums or c in symbols and c != '0':
                res_str += c
                can_zero = True
        integer = int(res_str)
        return integer
