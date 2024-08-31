class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = str(x)
        for i in range(int(len(num)/2)):
            if num[i] != num[-(1 + i)]:
                return False
        return True