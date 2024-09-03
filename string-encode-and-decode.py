class Solution:

    def encode(self, strs: List[str]) -> str:
        single = ""
        
        for i in strs:
            length = len(i)
            if length < 10:
                single += "00" + str(length) + i
            elif length < 100:
                single += "0" + str(length) + i
            else:
                single += str(length) + i
        return single

    def decode(self, s: str) -> List[str]:
        seperate = []
        i = 0

        while i < len(s):
            length = int(s[i:i + 3])
            seperate.append(s[i + 3: i + 3 + length])
            i += 3 + length

        return seperate