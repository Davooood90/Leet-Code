class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sequence = {}
        topstring = 0
        temp = 0
        stringhead = 0
        for i,char in enumerate(s):
            if (char not in sequence) or (sequence[char]<stringhead):
                temp += 1
                sequence[char] = i
            else:
                temp = (i-sequence[char])
                stringhead = sequence[char]+1
                sequence[char] = i
            if temp > topstring:
                topstring = temp
        return topstring