grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def print_table():
    for i in range(0, 3):
        print("|".join(list(map(str, grid[i]))) + "\n-----" if i != 2 else "|".join(list(map(str, grid[i]))))

def insert(num,  s):
    row = num // 3
    col = num % 3
    if grid[row][col] == "X" or grid[row][col] == "O": return False
    grid[row][col] = s
    return True

def check(s):
    for i in range(0, 3):
        if grid[i][0] == grid[i][1] == grid[i][2] == s or grid[0][i] == grid[1][i] == grid[2][i] == s: return True
    if grid[0][0] == grid[1][1] == grid[2][2] == s or grid[0][2] == grid[1][1] == grid[2][0] == s: return True
    return False

print("\n\n\n\n\n\n\n")
for i in range(0, 9):
    print("\033[F\x1b[2K\033[F\033[F\033[F\033[F\033[F\033[F\033[F", end = "")
    print()
    print_table()
    print()
    if i % 2 == 0:
        x = int(input("Player1 (X): "))
        while not insert(x - 1, "X"): x = int(input("Player1 (X):"))
        if check("X"):
            print("X won!")
            break
    else:
        x = int(input("Player2 (O): "))
        while not insert(x - 1, "O"): x = int(input("Player1 (O):"))
        if check("O"):
            print("O won!")
            break
