"""
Sudoku board validation algorithm 
You have been tasked with developing an algorithm to validate a 9 x 9 Sudoku board. Your algorithm needs to verify the validity of the filled cells on the board, adhering to the following conditions:
Every row should contain the numbers 1-9 exactly once, without repetition.
Every column should contain the numbers 1-9 exactly once, without repetition.
Each of the nine 3 x 3 sub-boxes within the grid should contain the numbers 1-9 exactly once, without repetition.
Can you outline an algorithm or a step-by-step approach to determine if the given Sudoku board configuration is valid based on these conditions?
Important Note: Ensure that you save your solution before progressing to the next question and before submitting your answer.
Exercise-1
Input :
9
5 3 . . 7 . . . .
6 . . 1 9 5 . . .
. 9 8 . . . . 6 .
8 . . . 6 . . . 3
4 . . 8 . 3 . . 1
7 . . . 2 . . . 6
. 6 . . . . 2 8 .
. . . 4 1 9 . . 5
. . . . 8 . . 7 9
Output : YES
Exercise-2
Input:
9
5 3 . . 7 . . . .
5 . . 1 9 5 . . .
. 9 8 . . . . 6 .
8 . . . 6 . . . 3
4 . . 8 . 3 . . 1
7 . . . 2 . . . 6
. 6 . . . . 2 8 .
. . . 4 1 9 . . 5
. . . . 8 . . 7 9
Output: NO

"""
def is_valid_sudoku(board):
    def is_valid_unit(unit):
        seen = set()
        for num in unit:
            if num != '.':
                if num in seen:
                    return False
                seen.add(num)
        return True

    for i in range(9):
        if not (is_valid_unit(board[i]) and
                is_valid_unit([board[j][i] for j in range(9)]) and
                is_valid_unit([board[r][c] for r in range(i // 3 * 3, i // 3 * 3 + 3) for c in range(i % 3 * 3, i % 3 * 3 + 3)])):
            return "NO"
    return "YES"


n = int(input())
sudoku_board = []
for _ in range(n):
    row = input().split()
    sudoku_board.append(row)
result = is_valid_sudoku(sudoku_board)
print(result)
