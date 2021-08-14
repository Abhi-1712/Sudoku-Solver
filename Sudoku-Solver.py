# Sudoku-Solver
def sudoku_solve():
    global puzzle
    for row in range(9):
        for column in range(9):
            if puzzle[row][column] == 0:
                for possible_number in range(1, 10):
                    if check(row, column, possible_number):
                        puzzle[row][column] = possible_number
                        sudoku_solve()
                        puzzle[row][column] = 0
                return
    display_solution()


def check(row, column, possible_number):
    for j in range(9):
        if puzzle[row][j] == possible_number:
            return False
    for k in range(9):
        if puzzle[k][column] == possible_number:
            return False
    row_start_point = (row // 3) * 3
    column_start_point = (column // 3) * 3
    for r in range(0, 3):
        for c in range(0, 3):
            if puzzle[r + row_start_point][c + column_start_point] == possible_number:
                return False
    return True


def display_solution():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    for a in range(9):
        for b in range(9):
            print(puzzle[a][b], end=' ')
        print()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


print("Enter the Sudoku Puzzle(enter 0 in place of empty blocks): ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
puzzle = []
for i in range(9):
    x = list(map(int, input().split()))
    puzzle.append(x)
sudoku_solve()
print("The above displayed is/are possible solution/s")
print("Thank you for using Sudoku Solver!!!")
