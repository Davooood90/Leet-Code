class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columns = {
            0: [],
            1: [],
            2: [],
            3: [],
            4: [],
            5: [],
            6: [],
            7: [],
            8: [],
        }

        for j, i in enumerate(board):
            row = []
            for x, y in enumerate(i):
                if y in row and y != ".":
                    return False
                elif y in columns[x] and y != ".":
                    return False
                row.append(y)
                columns[x].append(y)
            if (j + 1)% 3 == 0:
                for c in range(1, 4):
                    chunk = columns[c * 3 - 3][j - 2:j+1] + columns[c * 3 - 2][j - 2:j+1] + columns[c * 3 - 1][j - 2:j+1]
                    blanks = chunk.count(".")
                    if blanks == 0 and len(set(chunk)) != 9:
                        return False
                    elif len(set(chunk)) != 9 - blanks + 1:
                       return False
        return True