class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return(s)
        out = ""
        for j in range(numRows):
            for i in range(j, len(s), numRows * 2 - 2):
                out = out + s[i]
                x = i + (numRows * 2 - (2 * (j + 1)))
                if numRows * 2 > numRows * 2 - (2 * j) > 2 and x < len(s):
                    out = out + s[x]
        return(out)
                       