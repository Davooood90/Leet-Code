class Solution:
    def reverse(self, x: int) -> int:
        number = [1, ""]
        for i in str(x):
            if i == "-":
                number[0] = -1
            else:
                number[1] = i + number[1]
        final = number[0] * int(number[1])
        if final < -2 ** 31 or final > (2 ** 31 - 1):
            return 0
        else:
            return final
