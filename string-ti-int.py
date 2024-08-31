class Solution:
    def myAtoi(self, s: str) -> int:
        m = s.lstrip()
        if m == "":
            return 0
        num = m[0]
        for i in m[1::]:
            if i.isdigit():
                num += i
            else:
                break
        try:
            num = int(num)
        except:
            num = 0

        if num < -2 ** 31:
            return -2 ** 31
        elif num > 2 ** 31 - 1:
            return 2 ** 31 - 1
        else:
            return num