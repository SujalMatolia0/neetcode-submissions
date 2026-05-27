class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(len(board)):
            for j in range(len(board[i])):

                if board[i][j] == '.':
                    continue

                for b in range(len(board[i])):

                    if b == j:
                        continue

                    if board[i][b] == board[i][j]:
                        return False

                for c in range(len(board)):

                    if c == i:
                        continue

                    if board[c][j] == board[i][j]:
                        return False

                s = (i // 3) * 3
                t = (j // 3) * 3

                for d in range(s, s + 3):
                    for e in range(t, t + 3):

                        if d == i and e == j:
                            continue

                        if board[d][e] == board[i][j]:
                            return False

        return True